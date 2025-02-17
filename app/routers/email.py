from fastapi import APIRouter
from services.email_body_service import EmailBodyService
from services.email_title_service import EmailTitleService
from models.call_request import CallRequest, EmailResponse

email_router = APIRouter()

@email_router.post('/email')
def generate_email(request: CallRequest) -> EmailResponse:
    email_body = EmailBodyService.generate_email_body(request)
    email_title = EmailTitleService.generate_email_title(email_body)
    return {
        "title": email_title,
        "body": email_body
    }