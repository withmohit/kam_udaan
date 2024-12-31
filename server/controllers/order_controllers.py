from fastapi import HTTPException

from services.order_service import add_order, get_orders_summary,get_orders_summary_by_id

def make_order(lead_id, data):
    try:
        return add_order(lead_id, data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def get_orders():
    try:
        return get_orders_summary()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def get_orders_by_id(lead_id):
    try:
        return get_orders_summary_by_id(lead_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    