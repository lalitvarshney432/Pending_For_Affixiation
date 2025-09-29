from sqlalchemy.orm import Session
from models.user import User

def get_user_by_loginname(db: Session, userloginname: str):
    return db.query(User).filter(User.userloginname == userloginname).first()


def create_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
