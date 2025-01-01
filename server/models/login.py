from pydantic import BaseModel

class Login(BaseModel):
    kam_id: str
    password: str