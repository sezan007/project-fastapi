from sqlalchemy import Integer,String,Boolean,Column,ForeignKey
from sqlalchemy.sql.expression import null,text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,nullable=False)
    email=Column(String,nullable=False,unique=True)
    password=Column(String,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    phone_num=Column(String)
class post(Base):
    __tablename__="posts"
    id=Column(Integer,primary_key=True,nullable=False)
    title=Column(String,nullable=False)
    content=Column(String,nullable=False)
    published=Column(Boolean,server_default='True')
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    owner_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    owner = relationship("User")
class vote(Base):
    __tablename__="votes"
    post_id=Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True)
    user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)