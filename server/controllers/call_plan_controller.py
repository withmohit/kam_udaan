from datetime import datetime, timedelta
from fastapi import HTTPException
from services.call_plan_service import update_first, update_this

def first_call_plan(lead_id, data):
    try:
        last_date = datetime.now().strftime('%Y-%m-%d')
        last_date_obj = datetime.strptime(last_date, '%Y-%m-%d')
        next_date = (last_date_obj + timedelta(days=data.freq)).strftime('%Y-%m-%d')
        update_first(lead_id, last_date, next_date)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return {"message": "Call plan added successfully!"} 

def update_call_plan(lead_id, data):
    try:
        last_date = datetime.now().strftime('%Y-%m-%d')
        last_date_obj = datetime.strptime(last_date, '%Y-%m-%d')
        next_date = (last_date_obj + timedelta(days=data.freq)).strftime('%Y-%m-%d')
        update_this(lead_id, last_date, next_date)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return {"message": "Call plan updated successfully!"}