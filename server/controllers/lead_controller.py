from fastapi import HTTPException
from services.lead_service import add_lead, get_all_leads

def create_lead(data):
    try:
        return add_lead(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def fetch_all_leads():
    return get_all_leads()
