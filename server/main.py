from fastapi import FastAPI
from routes.lead_routes import router as lead_router

app = FastAPI()

# Register routes
app.include_router(lead_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Lead Management System!"}
