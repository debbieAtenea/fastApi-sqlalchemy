from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class usersFast(base):
    __tablename__ = "users_fast"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    token = Column(String)

usersFast()