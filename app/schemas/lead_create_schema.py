from pydantic import BaseModel,ConfigDict

class LeadCreate(BaseModel):
    name : str
    email : str
    company : str
    source : str

    model_config = ConfigDict(from_attributes = True)
    