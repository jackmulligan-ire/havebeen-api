from models.call_request import CallRequest
from huggingface_hub import InferenceClient
from langchain_core.prompts import ChatPromptTemplate


class EmailBodyGenerator():
    chat_model = InferenceClient(
        model = "meta-llama/Llama-3.2-3B-Instruct",
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
    def _chat_completion(cls, messages):
        return cls.chat_model.chat_completion(
            messages,
            temperature = 0.75,
            max_tokens= 300
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
        return EmailBodyGenerator._format_request | self._prompt_template | EmailBodyGenerator._extract_messages | EmailBodyGenerator._chat_completion | EmailBodyGenerator._extract_response