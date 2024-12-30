from fastapi import APIRouter
from controllers.interaction_controller import add_interaction
from models.interaction import Interaction

router = APIRouter()

@router.post("/leads/{lead_id}/interactions/")
async def interaction(lead_id: int, data: Interaction):
    return add_interaction(lead_id, data)