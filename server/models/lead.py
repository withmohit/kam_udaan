from pydantic import BaseModel

class Lead(BaseModel):
    restaurant_name: str
    address: str
    frequency: int