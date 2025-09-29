from sqlalchemy.orm import Session
from repositories import hsrp_states_repo

def get_all_states(db: Session):
    return hsrp_states_repo.get_all_states(db)

def get_hsrp_states_from_cache_or_all(db: Session):
    return hsrp_states_repo.get_hsrp_states_from_cache_or_all(db)

def get_states_by_state_id(db: Session, state_id: int):
    return hsrp_states_repo.get_states_by_state_id(db, state_id)
