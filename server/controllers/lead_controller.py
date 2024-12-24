from fastapi import HTTPException
from services.lead_service import add_lead, get_all_leads, add_pocs, get_pocs

def create_lead(data):
    try:
        return add_lead(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def fetch_all_leads():
    return get_all_leads()

def creat_pocs(lead_id,data):
    try:
        return add_pocs(lead_id,data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def fetch_all_pocs(lead_id):
    return get_pocs(lead_id)