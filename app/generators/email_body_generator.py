from models import CallRequest, EmailBodyModificationRequest
from huggingface_hub import HfApi
from langchain_core.prompts import ChatPromptTemplate
from typing import Union


class EmailBodyGenerator():
    endpoint = HfApi().get_inference_endpoint("llama-3-2-3b-instruct-havebeen")

    @classmethod
    def _format_request(cls, request: Union[CallRequest, EmailBodyModificationRequest]):
        output_string = ""
        for key, value in dict(request).items():
            if value: output_string += f"{key}: {value}\n"

        return output_string
    
    @classmethod
    def _extract_messages(cls, prompt_value):
        return [{"content": message.content, "role": message.type} for message in prompt_value.to_messages()]
    
    @classmethod
    def _chat_completion(cls, messages):
        return cls.endpoint.client.chat_completion(
            messages,
            temperature = 0.75,
            max_tokens = 300
        )

    @classmethod
    def _extract_response(cls, chat_completion_output):
        return chat_completion_output["choices"][0]["message"]["content"]
    
    def __init__(self, system_prompt):
        self._prompt_template = ChatPromptTemplate([
            ("system", system_prompt),
            ("user", "{user_input}")
        ])

    def get_chain(self):
        return self._format_request | self._prompt_template | self._extract_messages | self._chat_completion | self._extract_response