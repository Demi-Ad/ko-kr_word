from pydantic import BaseModel


class WordBase(BaseModel):

    ID: int
    WORD: str

    class Config:
        orm_mode = True


class User(BaseModel):
    user_name: str
    point: int

    class Config:
        orm_mode = True


class UserCreate(User):
    pass


class UserUpdate(User):
    pass
