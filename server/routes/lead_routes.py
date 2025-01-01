from fastapi import APIRouter, Header, HTTPException
from controllers.lead_controller import create_lead, fetch_all_leads
from models.lead import Lead

router = APIRouter()

@router.post("/leads/")
async def add_lead_endpoint(data: Lead,kam_id: int = Header(None)):
    if kam_id is None:
        raise HTTPException(status_code=400, detail="Missing KAM ID")
    return create_lead(data,kam_id)

@router.get("/leads/")
async def get_leads_endpoint(kam_id: int = Header(None)):
    if kam_id is None:
        raise HTTPException(status_code=400, detail="Missing KAM ID")
    return fetch_all_leads(kam_id)
