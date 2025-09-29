from pydantic import BaseModel, ConfigDict
from datetime import datetime

class UserLogin(BaseModel):
    userloginname: str
    password: str

class UserOut(BaseModel):
    userloginname: str
    userfirstname: str
    userlastname: str

    model_config = ConfigDict(from_attributes=True)

class UserRegister(BaseModel):
    hsrp_state_id: int
    userfirstname: str
    userlastname: str  
    userloginname: str
    password: str
    activestatus: int
    firstloginstatus: int
    created_timestamp: datetime
    
class Token(BaseModel):
    access_token: str
    user: UserOut