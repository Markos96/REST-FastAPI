from datetime import datetime
from typing import Union
from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    name: str
    age: int
    address: str
    created: datetime = datetime.now()


class UserDetails(BaseModel):
    username: str
    password: str
    name: str

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    name: str = None
    age: int = None
    address: str = None


class Login(BaseModel):
    username: str
    password: str


