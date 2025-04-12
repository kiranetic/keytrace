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
"""
You are a smart content extraction assistant.

Given a prompt that includes:
1. A list of keywords
2. A web page's content

You must return a structured response that maps each keyword to all matching sentences from the content.
Do not rephrase or mention things not discussed in the content. Only return sentences that **explicitly appear** in the content.
Always respond with a list of JSON objects, each containing the keyword and the list of matched sentences.
"""
    )

    agent = AssistantAgent(
        name="keytrace_agent",
        model_client=model_client,
        system_message=system_prompt,
    )

    return agent

