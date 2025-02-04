from models.call_request import CallRequest, EmailResponse
from services.chains.email_chain import EmailChain
import json

class EmailService():
    @classmethod
    def generate_email(cls, request: CallRequest) -> EmailResponse:
        chain = EmailChain.get_chain()
        result = chain.invoke(request)
        return json.loads(result)