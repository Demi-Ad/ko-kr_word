from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base


class Word(Base):

    __tablename__ = "word_list"

    ID = Column(Integer, primary_key=True, index=True)
    WORD = Column(String)
    START_WORD = Column(String, index=True)


class User(Base):
    __tablename__ = "users"

    user_name = Column(String, primary_key=True, index=True)
    point = Column(Integer)

