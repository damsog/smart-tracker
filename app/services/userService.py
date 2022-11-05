from prisma import Prisma
from ..models.userDTO import UserDTO, UserBaseDTO, UserUpdateDTO, UserCreateDTO
from typing import List

class UserService:
    def __init__(self, database: Prisma):
        self.database = database

    def get_all(self) -> List[UserDTO]:
        users = self.database.user.find_many()
        return users

    def get_by_id(self, id: str) -> UserDTO:
        user = self.database.user.find_unique(
            where={"id": id}
        )
        return user

    def create(self, user: UserCreateDTO) -> UserDTO:
        user = self.database.user.create(
            data=user.dict()
        )
        return user
    
    def update(self, id: str, user: UserUpdateDTO) -> UserDTO:
        user = self.database.user.update(
            data=user.dict(), 
            where={"id": id}
        )
        return user
    
    def delete(self, id: str) -> UserDTO:
        user = self.database.user.delete(
            where={"id": id}
        )