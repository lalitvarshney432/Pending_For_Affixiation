from fastapi import APIRouter, Depends
from app.api.deps import get_current_user




states = ["Maharashtra", "Gujarat", "Delhi", "Karnataka"]

@router.get("/states")
def get_states(current_user: str = Depends(get_current_user)):
    return {"states": states}

@router.get("/data")
def get_data(current_user: str = Depends(get_current_user)):
    return {"message": f"Hello, {current_user}"}


