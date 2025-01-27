from app.models.call_request import CallRequest, EmailResponse
from app.services.chains.email_chain import EmailChain

class EmailService():
    @classmethod
    def generate_email(cls, request: CallRequest) -> EmailResponse:
        chain = EmailChain.get_chain()
        result = chain.invoke(request)
        return result