from prisma import Prisma
from ..models.userDTO import UserDTO, UserBaseDTO, UserUpdateDTO, UserCreateDTO
from typing import List
from ..libs.logger import Logger
import asyncio

class UserService:
    def __init__(self, database: Prisma):
        self.database = database
        self.logger = Logger("INFO", "userService")

    async def get_all(self) -> List[UserDTO]:
        users = await self.database.user.find_many()
        return users

    async def get_by_id(self, id: str) -> UserDTO:
        user = await self.database.user.find_unique(
            where={"id": id}
        )
        return user

    async def create(self, user: UserCreateDTO) -> UserDTO:
        user = await self.database.user.create(
            data=user.dict()
        )
        return user
    
    # Updates user. updates fields that are not None. otherwises, 
    # keeps the old value
    async def update(self, id: str, user: UserUpdateDTO) -> UserDTO:
        user_dict = user.dict()
        
        # Gets current user data
        user_current = await self.database.user.find_unique(
            where={"id": id}
        ) 
        if(not user_current): return None
        user_current_dict = user_current.dict()

        # If incomming data is null, keep current data
        for key in user_dict:
            if user_dict[key] is None:
                user_dict[key] = user_current_dict[key]
        
        # Update user
        user_updated = await self.database.user.update(
            data=user_dict, 
            where={"id": id}
        )
        return user_updated
    
    async def delete(self, id: str) -> UserDTO:
        user = await self.database.user.delete(
            where={"id": id}
        )