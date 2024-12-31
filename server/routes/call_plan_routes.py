from fastapi import APIRouter
from controllers.call_plan_controller import get_call_plan

router = APIRouter()

@router.get("/leads/call-plan/")
async def get_pending_calls():
    return get_call_plan()