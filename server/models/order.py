from pydantic import BaseModel

class Order(BaseModel):
    order_amount: float