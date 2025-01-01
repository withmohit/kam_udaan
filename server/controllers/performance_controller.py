from fastapi import HTTPException

from services.performance_service import leads_performance

def get_performance(kam_id):
    try:
        return leads_performance(kam_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))