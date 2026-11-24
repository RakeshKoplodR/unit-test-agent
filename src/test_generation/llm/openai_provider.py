from langchain_openai import ChatOpenAI

class ChatAIProvider:

    @staticmethod
    def get_llm():
        return ChatOpenAI(
            model="gpt-6-luna",
            temperature=1
        )