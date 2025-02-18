from pydantic import BaseModel

class OutlineRequest(BaseModel):
    outline: str

class SaveRequest(BaseModel):
    text: str
