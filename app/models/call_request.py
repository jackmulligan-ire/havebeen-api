from typing import Optional
from pydantic import BaseModel

class CallRequest(BaseModel):
    title: str
    description: str
    length: Optional[int] = None

class EmailResponse(BaseModel):
    title: str
    body: str