from fastapi import HTTPException
from services.call_plan_service import pending_calls


def get_call_plan(lead_id):
    try:
        return pending_calls(lead_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))