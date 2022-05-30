from datetime import date
from pydantic import BaseModel


class Role_Create(BaseModel):
    name: str

    class Config:
        orm_mode = True


class Role_for_User(BaseModel):
    id: int


class UserRole(BaseModel):
    user_id: int
    role_id: int
    is_active: bool
    date_created: date

    class Config:
        orm_mode = True


class UserRoleResponse(BaseModel):
    user_role: UserRole
    name: str

    class Config:
        orm_mode = True


class User_In_DB(BaseModel):
    username: str
    password: str
    email: str
    department_id: int
    roles: list[int]

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    username: str
    roles: list[int]
    department_id: int
    department_level: int

    class Config:
        orm_mode = True


class Department(BaseModel):
    description: str
    department_level: int

    class Config:
        orm_mode = True
