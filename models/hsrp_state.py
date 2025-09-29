from sqlalchemy import Column, Integer, String
from db.base import Base

class HsrpState(Base):
    __tablename__ = "HSRPStates"

    hsrp_state_id = Column("HSRPStateID", Integer, primary_key=True, index=True)
    state_name = Column("StateName", String(100), nullable=False)
    # add other columns as per your DB schema
