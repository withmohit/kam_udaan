from pydantic import BaseModel

class Lead(BaseModel):
    restaurant_name: str
    address: str
    contact_number: str
    current_status: str
    assigned_kam: str

class Contact(BaseModel):
    person_name: str
    role: str
    phone_number: str
    email: str
    lead_id: int