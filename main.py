from fastapi import FastAPI
from api import routes_auth,routes_states, routes_BMHSRP,routes_hsrp_states
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="FastAPI Web App")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(routes_auth.router, prefix="/auth", tags=["auth"])
app.include_router(routes_states.router, prefix="/api", tags=["states"])
app.include_router(routes_hsrp_states.router, prefix="/api", tags=["HSRP States"])
app.include_router(routes_BMHSRP.router, prefix="/api", tags=["Dealer Details"])




@app.get("/health")
def health():
    return {"status": "healthy"}


