from pydantic import BaseModel

class Lead(BaseModel):
    restaurant_name: str
    address: str
    frequency: int
    order_count: int
    current_status: str
    assigned_kam: str
