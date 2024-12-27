from fastapi import FastAPI
from routes.lead_routes import router as lead_router
from routes.call_plan_routes import router as call_plan_router
from routes.pcos_routes import router as pcos_router

app = FastAPI()

# Register routes
app.include_router(lead_router)
app.include_router(call_plan_router)
app.include_router(pcos_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Lead Management System!"}
