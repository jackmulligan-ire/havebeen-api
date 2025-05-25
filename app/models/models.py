from typing import Optional
from pydantic import BaseModel

class CallRequest(BaseModel):
    title: str
    description: str
    length: Optional[int] = None

class EmailBodyModificationRequest(BaseModel):
    body: str
    user_request: str

class EmailResponse(BaseModel):
    title: str
    body: str

class EmailBodyModificationResponse(BaseModel):
    body: str

class EmailBody(str): pass
class EmailTitle(str): pass