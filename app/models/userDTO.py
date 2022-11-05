from pydantic import BaseModel
from typing import Optional

class UserBaseDTO(BaseModel):
    name: str
    email: str
    password: str
    firstName: str
    lastName: str
    image: str


class UserCreateDTO(UserBaseDTO):
    pass

class UserUpdateDTO(BaseModel):
    name: Optional[str]
    email: Optional[str]
    password: Optional[str]
    firstName: Optional[str]
    lastName: Optional[str]
    image: Optional[str]

class UserDTO(UserBaseDTO):
    id: str
    emailVerified: bool
    createdAt: str
    updatedAt: str
    class Config:
        orm_mode = True
