from fastapi import APIRouter
from controllers.pocs_controller import creat_pocs, fetch_all_pocs
from models.pocs import Contact

router = APIRouter()

@router.post("/leads/{lead_id}/contacts/")
async def add_lead_pocs(lead_id: int, data:Contact):
    return creat_pocs(lead_id, data)

@router.get("/leads/{lead_id}/contacts/")
async def get_lead_pocs(lead_id: int):
    return fetch_all_pocs(lead_id)