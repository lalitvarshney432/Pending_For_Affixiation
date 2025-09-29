from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.deps import get_db
from services import hsrp_states_service

router = APIRouter()

@router.get("/hsrp/states")
def get_all_states(db: Session = Depends(get_db)):
    return hsrp_states_service.get_all_states(db)

@router.get("/hsrp/states/{state_id}")
def get_states_by_state_id(state_id: int, db: Session = Depends(get_db)):
    result = hsrp_states_service.get_states_by_state_id(db, state_id)
    if not result:
        raise HTTPException(status_code=404, detail="State not found")
    return result
