from models.call_request import CallRequest
from services.chains.email_chain_prompt_template import prompt_template
from huggingface_hub import InferenceClient

class EmailChain():
    chat_model = InferenceClient(
        model = "microsoft/Phi-3-mini-4k-instruct",
    )

    @classmethod
    def _format_request(cls, request: CallRequest):
        output_string = ""
        for key, value in dict(request).items():
            if value: output_string += f"{key}: {value}\n"

        return output_string
    
    @classmethod
    def _extract_messages(cls, prompt_value):
        return [{"content": message.content, "role": message.type} for message in prompt_value.to_messages()]

    @classmethod
    def _extract_response(cls, chat_completion_output):
        return chat_completion_output["choices"][0]["message"]["content"]

    @classmethod
    def get_chain(cls):
        return EmailChain._format_request | prompt_template | EmailChain._extract_messages | EmailChain.chat_model.chat_completion | EmailChain._extract_response