from fastapi import HTTPException
from services.pocs_service import add_pocs, get_pocs

def creat_pocs(lead_id,data):
    try:
        return add_pocs(lead_id,data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def fetch_all_pocs(lead_id):
    return get_pocs(lead_id)