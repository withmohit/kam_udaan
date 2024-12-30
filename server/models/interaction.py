from pydantic import BaseModel

class Interaction(BaseModel):
    notes: str
    type: str
    