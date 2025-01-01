from fastapi import APIRouter
from controllers.interaction_controller import add_interaction, get_interactions
from models.interaction import Interaction

router = APIRouter()

# kam_id = Header(None)

@router.post("/leads/{lead_id}/interactions/")
async def interaction(lead_id: int,data: Interaction):
    return add_interaction(lead_id ,data)

@router.get("/leads/{lead_id}/interactions/")
async def interactions(lead_id: int):
    return get_interactions(lead_id)