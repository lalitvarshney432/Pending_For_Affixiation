
from pydantic import BaseModel
from datetime import date

class AppointmentQuery(BaseModel):
    from_date: str
    to_date: str
    state_id: int
    delivery_type: str

class HsrpSearch(BaseModel):
    Search: str 
    
class TatSummaryQuery(BaseModel):
    state_id: int
    from_date: str
    to_date: str    
    ec_type: str
    ec_id: str
    tat_version: str
    report_type: str
    ec_name: str
    
class TatSummaryDownload(BaseModel):
    state_id: str
    from_date: str
    to_date: str    
    report_type: str
    date_tat:str
    date_order:str 
    tat_version: str
    ec_name: str
    
class DealerOutstandingOemWise(BaseModel):
    state_id: int
    from_date: str
    oem_id: int
    oem_name: str

class BussinessReport(BaseModel):
    state_id: str
    from_date: str
    to_date: str
    selected_report: str
    
class OrderWiseReport(BaseModel):
    state_id: str
    from_date: str
    to_date: str

class OrderWiseCountReport(BaseModel):
    state_id: int
    from_date: str
    to_date: str
    
class MobileOTPTrackerReport(BaseModel):
    select_type_wise:str
    state_id: str
    select_type:str
    from_date:str
    to_date:str  
    
class RabmReport(BaseModel):
    state_id: str
    from_date:str
    to_date:str
    hub_id:str
    type_id:str 
    
class OrderWiseReportColumn(BaseModel):
    state_id: int
    from_date: str
    to_date: str
    column_name:str
      
class TatEcName(BaseModel):
    HsrpStateId: int
    ECType: str