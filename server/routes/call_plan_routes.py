from fastapi import APIRouter, Header
from controllers.call_plan_controller import get_call_plan

router = APIRouter()

@router.get("/leads/call-plan/")
async def get_pending_calls(kam_id: int = Header(None)):
    if kam_id is None:
        return {"error": "Missing KAM ID"}
    return get_call_plan(kam_id)