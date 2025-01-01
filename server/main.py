from fastapi import FastAPI
from routes.lead_routes import router as lead_router
from routes.call_plan_routes import router as call_plan_router
from routes.pcos_routes import router as pcos_router
from routes.interactions_routes import router as interaction_router
from routes.order_routes import router as order_router
from routes.performance import router as performance_router
from routes.login_routes import router as login_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for your frontend origin
origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(lead_router)
app.include_router(call_plan_router)
app.include_router(pcos_router)
app.include_router(interaction_router)
app.include_router(order_router)
app.include_router(performance_router)
app.include_router(login_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Lead Management System!"}
