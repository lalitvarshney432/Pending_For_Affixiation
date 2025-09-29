from sqlalchemy.orm import Session
from repositories import user_repo
from core import security
from models.user import User
from datetime import datetime

def authenticate_user(db: Session, userloginname: str, password: str):
    """
    Authenticate user by userloginname and password.
    Returns the user object if credentials are correct, else None.
    """
    db_user = user_repo.get_user_by_loginname(db, userloginname)
    if not db_user or not security.verify_password(password, db_user.password):
        return None
    return db_user

def register_user(
    db: Session,
    hsrp_state_id: int,
    userloginname: str,
    password: str,
    first_name: str,
    last_name: str,
    activestatus: int,
    firstloginstatus: int,
    created_timestamp: datetime
) -> User:
    """
    Registers a new user with all NOT NULLABLE fields.

    Args:
        db (Session): SQLAlchemy database session.
        hsrp_state_id (int): HSRP State ID.
        userloginname (str): Unique user login name.
        password (str): Plain text password to hash.
        first_name (str): User's first name.
        last_name (str): User's last name.
        activestatus (int): Active status flag.
        firstloginstatus (int): First login status flag.
        created_timestamp (datetime): Created timestamp.

    Returns:
        User: Newly created User object.
    """
    hashed_pwd = security.hash_password(password)

    new_user = User(
        hsrp_state_id=hsrp_state_id,
        userloginname=userloginname,
        password=hashed_pwd,
        userfirstname=first_name,
        userlastname=last_name,
        activestatus=activestatus,
        firstloginstatus=firstloginstatus,
        created_timestamp=created_timestamp
    )

    return user_repo.create_user(db, new_user)

