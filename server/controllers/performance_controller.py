from fastapi import HTTPException

from services.performance_service import leads_performance

def get_performance():
    try:
        return leads_performance()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))