from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "ReactHoUsers"
    id = Column("UserID", Integer, primary_key=True, index=True)
    hsrp_state_id = Column("HSRP_StateID", Integer, nullable=False)
    userloginname = Column("UserLoginName", String(100), unique=True, index=True, nullable=False)
    password = Column("Password", String(255), nullable=False)
    userfirstname = Column("UserFirstName", String(50), nullable=False)
    userlastname = Column("UserLastName", String(50), nullable=True)
    activestatus = Column("ActiveStatus", Integer, nullable=False)
    firstloginstatus = Column("FirstLoginStatus", Integer, nullable=False)
    created_timestamp = Column("created_timestamp", DateTime, nullable=False)

    def __repr__(self):
        return f"<User(userloginname={self.userloginname}, userfirstname={self.userfirstname}, userlastname={self.userlastname})>"