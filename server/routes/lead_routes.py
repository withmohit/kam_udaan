from fastapi import APIRouter
from controllers.lead_controller import create_lead, fetch_all_leads
from models.lead import Lead

router = APIRouter()

@router.post("/leads/")
async def add_lead_endpoint(data: Lead):
    return create_lead(data)

@router.get("/leads/")
async def get_leads_endpoint():
    return fetch_all_leads()
