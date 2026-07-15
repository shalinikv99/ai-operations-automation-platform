from datetime import datetime
from pydantic import BaseModel,ConfigDict

class LeadResponse(BaseModel):
    id : int
    name : str
    email : str
    company : str
    source : str
    status : str
    priority : str
    ai_summary: str
    created_at : datetime

    model_config = ConfigDict(from_attributes = True)
    



