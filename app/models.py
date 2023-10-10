from .database import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import Relationship

class Question(Base):
    __tablename__='questions'
    id =Column(Integer,primary_key=True, nullable=False)
    question = Column(String,nullable=False)
    answer=Column(String,nullable=False)
    level=Column(Integer,nullable=True)

class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,nullable=False)
    email =Column(String,nullable=False,unique=True)
    password=Column(String,nullable=False)
    start_level =Column(Integer,nullable=True)
    current_level=Column(Integer,nullable=True,server_default='0')

class Review(Base):
    __tablename__='review'
    question_id=Column(Integer,ForeignKey('questions.id',ondelete="CASCADE"),primary_key=True)
    user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)
    result=Column(Boolean,server_default="False",nullable=False)

# class User_data(Base):
#     __tablename__='user_data'
#     user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)
#     start_level =Column(Integer,nullable=True)
#     current_level=Column(Integer,nullable=True,server_default='0')