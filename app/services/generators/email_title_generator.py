from huggingface_hub import InferenceClient
from langchain_core.prompts import ChatPromptTemplate


class EmailTitleGenerator():
    chat_model = InferenceClient(
        model = "mistralai/Mistral-7B-Instruct-v0.3",
    )
    
    @classmethod
    def _extract_messages(cls, prompt_value):
        return [{"content": message.content, "role": "user"} for message in prompt_value.to_messages()]
    
    @classmethod
    def _chat_completion(cls, messages):
        return cls.chat_model.chat_completion(
            messages,
            temperature = 1,
            max_tokens=15
        )

    @classmethod
    def _extract_response(cls, chat_completion_output):
        return chat_completion_output["choices"][0]["message"]["content"]
    
    def __init__(self, system_prompt):
        self._prompt_template = ChatPromptTemplate([
            ("user", system_prompt),
        ])

    def get_chain(self):
        return self._prompt_template | self._extract_messages | self._chat_completion | self._extract_response