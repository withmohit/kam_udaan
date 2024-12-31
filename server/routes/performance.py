from fastapi import APIRouter
from controllers.performance_controller import get_performance
router = APIRouter()

@router.get("/leads/performance/")
async def performance():
    return get_performance()