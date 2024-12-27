from pydantic import BaseModel

class CallPlan(BaseModel):
    freq: int