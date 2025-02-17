from fastapi import APIRouter
from services.email_body_service import EmailBodyService
from models.call_request import CallRequest, EmailResponse

email_router = APIRouter()

@email_router.post('/email')
def generate_email(request: CallRequest) -> EmailResponse:
    email_body = EmailBodyService.generate_email_body(request)
    return {
        "title": "Placeholder",
        "body": email_body
    }