from fastapi import HTTPException
from services.interaction_service import add_interaction_query

def add_interaction(lead_id, data):
    try:
        return add_interaction_query(lead_id, data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))