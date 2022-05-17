from pydantic import BaseModel


class Role_Create(BaseModel):
    name: str

    class Config:
        orm_mode = True

class Role_for_User(BaseModel):
    id: int


class User_In_DB(BaseModel):
    username: str
    password: str
    email: str
    roles: list[int]

    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    username: str

    class Config:
        orm_mode = True
