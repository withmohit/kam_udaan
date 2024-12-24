from fastapi import APIRouter
from controllers.lead_controller import create_lead, fetch_all_leads, creat_pocs, fetch_all_pocs
from models.lead import Lead, Contact

router = APIRouter()

@router.post("/leads/")
async def add_lead_endpoint(data: Lead):
    return create_lead(data)

@router.get("/leads/")
async def get_leads_endpoint():
    return fetch_all_leads()

@router.post("/leads/{lead_id}/contacts/")
async def add_lead_pocs(lead_id: int, data:Contact):
    return creat_pocs(lead_id, data)

@router.get("/leads/{lead_id}/contacts/")
async def get_lead_pocs(lead_id: int):
    return fetch_all_pocs(lead_id)