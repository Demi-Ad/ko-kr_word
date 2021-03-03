from sqlalchemy.orm import Session
import model
import schemas


def select_word(db: Session, word: str):
    return db.query(model.Word).filter(model.Word.WORD == word).first()


def get_word(db: Session, start_word: str):
    return db.query(model.Word).filter(model.Word.START_WORD == start_word).all()


def get_user(db: Session, name: str):
    return db.query(model.User).filter(model.User.user_name == name).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = model.User(user_name=user.user_name, point=0)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_name: str, update_point: int):
    user = db.query(model.User).filter(model.User.user_name == user_name).first()
    if user.point < update_point:
        user.point = update_point
        db.commit()
        db.refresh(user)
        return user
    else:
        pass


def user_rank(db: Session):
    return db.query(model.User).order_by(model.User.point.desc()).all()
