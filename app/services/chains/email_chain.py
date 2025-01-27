from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from app.models.call_request import CallRequest
from app.services.chains.email_chain_prompt_template import prompt_template
from langchain.schema.output_parser import StrOutputParser
from langchain_core.runnables import RunnableLambda

class EmailChain():
    chat_model = ChatHuggingFace(llm = HuggingFaceEndpoint(
        repo_id = "microsoft/Phi-3-mini-4k-instruct",
        max_tokens = 250,
        task = "text-generation",
    ))

    @classmethod
    def _format_request(cls, request: CallRequest):
        output_string = ""
        for key, value in dict(request).items():
            output_string += f"{key}: {value}\n"

        return output_string

    @classmethod
    def get_chain(cls):
        return RunnableLambda(EmailChain._format_request) | prompt_template | EmailChain.chat_model | StrOutputParser()