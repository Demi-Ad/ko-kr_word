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


@app.get("/users/{user_name}", response_model=schemas.UserGet)
def read_user(user_name: str, db: Session = Depends(get_db)):
    db_user = curd.get_user(db, name=user_name)
    return db_user


@app.get("/rank", response_model=List[schemas.UserGet])
def user_rank(db: Session = Depends(get_db)):
    return curd.user_rank(db=db)


@app.get("/word", response_model=List[schemas.WordBase])
def read_word(word: str, db: Session = Depends(get_db)):
    db_word = curd.get_word(db, start_word=word[-1])
    return db_word


@app.get("/check/{word}")
def select_word(word: str, db: Session = Depends(get_db)):
    db_word = curd.select_word(db, word)
    if db_word is not None:
        return True
    else:
        return False


@app.put("/users/{user_name}/{point}", response_model=schemas.UserUpdate)
def update_user(user_name: str, point: int, db: Session = Depends(get_db)):
    db_user = curd.update_user(db, user_name=user_name, update_point=point)
    return db_user
