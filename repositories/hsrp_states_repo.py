from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text
from fastapi import HTTPException
from queries.hsrp_states_queries import (
    GET_ALL_STATES,
    GET_STATES_BY_STATEID,
    GET_HSRP_STATES_FROM_CACHE_OR_ALL
)

def get_all_states(db: Session):
    try:
        result = db.execute(text(GET_ALL_STATES))
        return [dict(row) for row in result.mappings().all()]
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_states_by_state_id(db: Session, state_id: int):
    try:
        result = db.execute(text(GET_STATES_BY_STATEID), {"state_id": state_id})
        return [dict(row) for row in result.mappings().all()]
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_hsrp_states_from_cache_or_all(db: Session):
    try:
        result = db.execute(text(GET_HSRP_STATES_FROM_CACHE_OR_ALL))
        return [dict(row) for row in result.mappings().all()]
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))
