from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

class PostBase(BaseModel):
    title:str
    content:str
    published:bool=True
    ##rating: Optional[int]=None
class PostCreate(PostBase):
    pass
class User_Create(BaseModel):
    email:EmailStr
    password:str
class UserOut(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime
    class Config:
        orm_mode = True
class UserLogin(BaseModel):
    email:EmailStr
    password:str
class Token(BaseModel):
    access_token:str
    token_type:str
class Tokendata(BaseModel):
    id: Optional[int] = None
class Post(PostBase):
    id:int
    created_at:datetime
    owner_id:int
    owner:UserOut
    class Config:
        orm_mode = True
class Vote(BaseModel):
    post_id:int
    dir:conint(le=1)
class PostOut(BaseModel):
    post:Post
    votes:int
    class Config:
        orm_mode = True
