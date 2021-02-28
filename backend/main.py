from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import curd
import model
import schemas
from database import SessionLocal, engine
from typing import List

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return curd.create_user(db=db, user=user)


@app.get("/users/{user_name}", response_model=schemas.User)
def read_user(user_name: str, db: Session = Depends(get_db)):
    db_user = curd.get_user(db, name=user_name)
    return db_user


@app.get("/word/{start_word}", response_model=List[schemas.WordBase])
def read_word(word: str, db: Session = Depends(get_db)):
    db_word = curd.get_word(db, start_word=word[-1])
    return db_word


@app.put("/users/{user_name}/{point}", response_model=schemas.User)
def update_user(user_name: str, point: int, db: Session = Depends(get_db)):
    db_user = curd.update_user(db, user_name=user_name, update_point=point)
    return db_user
