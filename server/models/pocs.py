from pydantic import BaseModel

class Contact(BaseModel):
    person_name: str
    role: str
    phone_number: str
    email: str
    lead_id: int