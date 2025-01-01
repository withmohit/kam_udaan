from fastapi import APIRouter, Header
from controllers.performance_controller import get_performance
router = APIRouter()

@router.get("/leads/performance/")
async def performance(kam_id: int = Header(None)):
    if kam_id is None:
        return {"error": "Missing KAM ID"}
    return get_performance(kam_id)

# async def performance():
#     # if kam_id is None:
#     #     return {"error": "Missing KAM ID"}
#     return get_performance()