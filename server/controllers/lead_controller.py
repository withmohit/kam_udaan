from fastapi import HTTPException
from services.lead_service import add_lead, get_all_leads

def create_lead(data,kam_id):
    try:
        return add_lead(data,kam_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def fetch_all_leads(kam_id):
    return get_all_leads(kam_id)

