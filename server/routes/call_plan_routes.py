from fastapi import APIRouter
from controllers.call_plan_controller import first_call_plan, update_call_plan
from models.call_plan import CallPlan

router = APIRouter()

@router.post("/leads/{lead_id}/call_plan/")
async def add_lead_call_plan(lead_id: int,data: CallPlan):
    # data = None
    return first_call_plan(lead_id, data)

@router.patch("/leads/{lead_id}/call_plan/")
async def update_lead_call_plan(lead_id: int,data: CallPlan):
    # data = None
    return update_call_plan(lead_id, data)



