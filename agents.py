import os
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

load_dotenv()


def extraction_agent() -> AssistantAgent:

    model_client = OpenAIChatCompletionClient(
        model=os.getenv("OPENAI_MODEL"),
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    system_prompt = (
'''
You are a helpful assistant.
From the provided web content, extract a sentence that is either directly about the given keyword or closely related/relevent to it. 
Don't rephrase or mention things not discussed in the content.
Strictly base your response on the content.
If no relevant content is found, say None.
'''
    )

    agent = AssistantAgent(
        name="keytrace_agent",
        model_client=model_client,
        system_message=system_prompt,
    )

    return agent

