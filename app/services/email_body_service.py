from models import CallRequest, EmailBody
from generators.email_body_generator import EmailBodyGenerator
from services.system_prompt_service import SystemPromptService
from prompts.email_body_prompts import example_prompts, negative_prompts, task_prompts

class EmailBodyService():
    @classmethod
    def generate_email_body(cls, request: CallRequest) -> EmailBody:
        system_prompt_service = SystemPromptService([example_prompts, negative_prompts, task_prompts])
        system_prompt = system_prompt_service.get_system_prompt()
        email_body_generator = EmailBodyGenerator(system_prompt)
        email_body_chain = email_body_generator.get_chain()
        email_body = email_body_chain.invoke(request)
        return email_body