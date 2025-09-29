from sqlalchemy.orm import Session
from sqlalchemy import text
from datetime import date
from db.database import engine

def get_appointment_sp_name(state_id: int) -> str:
    if state_id == 20:
        return "AppointmentDatewiseReport1"
    elif state_id == 13:
        return "AppointmentDatewiseReportCG"
    else:
        return "AppointmentDatewiseReport"
    
def fetch_appointment_data(
    db : Session,
    from_date: str,
    to_date: str,
    state_id: int,
    delivery_type: str,
):
    sp_name = get_appointment_sp_name(state_id)

    conn = engine.raw_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            f"EXEC {sp_name} @fromDate=?, @toDate=?, @stateId=?, @deliveryType=?",
            (from_date, to_date, state_id, delivery_type)
        )

        # Loop until a result set with rows is found
        while True:
            if cursor.description:
                columns = [col[0] for col in cursor.description]
                rows = cursor.fetchall()
                result = [dict(zip(columns, row)) for row in rows]
                break
            if not cursor.nextset():
                result = []
                break

        cursor.close()
        conn.close()
        return result

    except Exception as e:
        conn.close()
        raise e
