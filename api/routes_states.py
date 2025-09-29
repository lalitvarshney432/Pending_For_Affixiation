from fastapi import APIRouter, Depends
from .deps import get_current_user
from sqlalchemy.orm import Session
from db.database import test_connection  


router = APIRouter()

states = ["Maharashtra", "Gujarat", "Delhi", "Karnataka"]

@router.get("/states")
def get_states(current_user: str = Depends(get_current_user)):
    return {"states": states}

