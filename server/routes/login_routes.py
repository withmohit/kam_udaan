from fastapi import APIRouter,HTTPException
from controllers.login_controller import login_kam
from models.login import Login

router=APIRouter()

@router.post("/login/")
async def login(data: Login):
    return login_kam(data)