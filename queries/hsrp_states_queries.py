GET_ALL_STATES = """
select HSRPStateName,HSRP_StateID
from HSRPState  
where ActiveStatus='Y' Order by HSRPStateName
"""

GET_STATES_BY_STATEID = """
select HSRPStateName,HSRP_StateID from HSRPState  
where HSRP_StateID=:state_id
and isBookMyHSRP='Y' and ActiveStatus ='Y' Order by HSRPStateName
"""

GET_HSRP_STATES_FROM_CACHE_OR_ALL = """
select HSRPStateName,HSRP_StateID from HSRPState  where ActiveStatus='Y' and isBookMyHSRP='Y' Order by HSRPStateName
"""

