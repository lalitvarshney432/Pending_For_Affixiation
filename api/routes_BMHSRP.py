from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import test_connection  # adjust if path differs
from schemas.report_schema import AppointmentQuery
from services.report_service import fetch_appointment_data

router = APIRouter()



@router.post("/hsrp/appointments")
def get_appointments(query: AppointmentQuery, db: Session = Depends(test_connection)):
    data = fetch_appointment_data(
        db,
        from_date=query.from_date,
        to_date=query.to_date,
        state_id=query.state_id,
        delivery_type=query.delivery_type
    )
    return {
        "success": True,
        "data": {
            "items": data
        }
    }