from huggingface_hub import HfApi
from langchain_core.prompts import ChatPromptTemplate


class EmailTitleGenerator():
    endpoint = HfApi().get_inference_endpoint("llama-3-2-3b-instruct-havebeen")
    
    @classmethod
    def _extract_messages(cls, prompt_value):
        return [{"content": message.content, "role": message.type} for message in prompt_value.to_messages()]
    
    @classmethod
    def _chat_completion(cls, messages):
        return cls.endpoint.client.chat_completion(
            messages,
            temperature = 0.5,
            max_tokens=15
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
        return self._prompt_template | self._extract_messages | self._chat_completion | self._extract_response