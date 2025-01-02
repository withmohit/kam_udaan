from fastapi import APIRouter, Header
from controllers.performance_controller import get_performance,get_pattern
router = APIRouter()

@router.get("/leads/performance/")
async def performance(kam_id: int = Header(None)):
    if kam_id is None:
        return {"error": "Missing KAM ID"}
    return get_performance(kam_id)

@router.get("/leads/performance/{lead_id}/pattern")
async def performance(lead_id:int):
    return get_pattern(lead_id)
