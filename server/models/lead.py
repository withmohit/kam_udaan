from pydantic import BaseModel

class Lead(BaseModel):
    restaurant_name: str
    address: str
    contact_number: str
    current_status: str
    assigned_kam: str
