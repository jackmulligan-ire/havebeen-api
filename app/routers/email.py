from fastapi import APIRouter
from app.services.email_service import EmailService
from app.models.call_request import CallRequest, EmailResponse

email_router = APIRouter()

@email_router.post('/email')
def generate_email(request: CallRequest) -> EmailResponse:
    email_response = EmailService.generate_email(request)
    return email_response