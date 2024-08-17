from langchain_openai import ChatOpenAI


def get_model():
    return ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
