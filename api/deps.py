from db.database import SessionLocal,SessionLocal1
from fastapi import Depends, HTTPException, Header
from typing import Optional
from core.security import verify_token

def get_current_user(Authorization: Optional[str] = Header(None)) -> str:
    if not Authorization:
        raise HTTPException(status_code=401, detail="Authorization header missing")
    
    if not Authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization header format")

    token = Authorization.split(" ")[1]
    try:
        payload = verify_token(token)
        return payload.get("sub")
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_test_db():
    db = SessionLocal1()
    try:
        yield db
    finally:
        db.close()