from sqlalchemy.orm import Session
import model
import schemas


def get_word(db: Session, start_word: str):
    """
    :param db: database
    :param start_word: word[-1]
    :return: wordlist
    """
    return db.query(model.Word).filter(model.Word.START_WORD == start_word).all()


def get_user(db: Session, name: str):
    return db.query(model.User).filter(model.User.user_name == name).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = model.User(user_name=user.user_name, point=user.point)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_name: str, update_point: int):
    user = db.query(model.User).filter(model.User.user_name == user_name).first()
    user.point = update_point
    db.commit()
    db.refresh(user)
    return user
