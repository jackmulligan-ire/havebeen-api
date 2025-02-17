from services.generators.email_title_generator import EmailTitleGenerator
from services.system_prompt_service import SystemPromptService
from prompts.email_title_prompts import example_prompts, negative_prompts, task_prompts

class EmailTitleService():
    @classmethod
    def generate_email_title(cls, email_body: str) -> str:
        system_prompt_service = SystemPromptService([example_prompts, negative_prompts, task_prompts])
        system_prompt = system_prompt_service.get_system_prompt()
        email_title_generator = EmailTitleGenerator(system_prompt)
        email_title_chain = email_title_generator.get_chain()
        email_title = email_title_chain.invoke(email_body)
        return email_title