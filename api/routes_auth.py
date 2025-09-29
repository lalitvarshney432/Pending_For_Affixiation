from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.user import UserLogin, Token, UserOut, UserRegister
from api.deps import get_test_db as get_db
from services import user_service
from core import security
from datetime import timedelta
from repositories import user_repo
from datetime import datetime


router = APIRouter()

@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = user_service.authenticate_user(db, user.userloginname, user.password)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = security.create_access_token(
        data={"sub": db_user.userloginname}
    )
    user_out = UserOut.model_validate(db_user)
    return {"access_token": access_token, "user": user_out}

@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):
    existing_user = user_repo.get_user_by_loginname(db, user.userloginname)
    if existing_user:
        raise HTTPException(status_code=400, detail="UserLoginName already registered")
    
    
    if not user.created_timestamp:
        user.created_timestamp = datetime.utcnow()
    
  
    new_user = user_service.register_user(
        db,
        user.hsrp_state_id,
        user.userloginname,
        user.password,
        user.userfirstname,
        user.userlastname,
        user.activestatus,
        user.firstloginstatus,
        user.created_timestamp
    )
    return {"message": f"User {new_user.userloginname} registered successfully"}