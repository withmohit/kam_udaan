from fastapi import APIRouter

from controllers.order_controllers import make_order, get_orders, get_orders_by_id
from models.order import Order

router=APIRouter()

@router.post("/leads/{lead_id}/orders/")
async def create_order(lead_id:int, data: Order):
    return make_order(lead_id, data)

@router.get("/leads/{lead_id}/orders/")
async def view_order():
    return get_orders_by_id()

@router.get("/leads/orders/")
async def all_orders():
    return get_orders()
