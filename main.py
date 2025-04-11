from crawler import crawl_init

import asyncio

async def run_assistant(msg):

    reply = await agent.on_messages([msg], cancellation_token=CancellationToken())

    print("reply:", str(reply))

    print("reply inner_messages", str(reply.inner_messages))

    print("reply chat_message", str(reply.chat_message))



keyword = "debit card"

url = "https://www.gov.uk/send-prisoner-money"

content = crawl_init(url)

# print(content)


prompt = f'''
You are a helpful keyword scrapper assistant. 
From the provided web content, extract a sentence or paragraph that is either directly about the given keyword or closely related/relevent to it.

Keyword: {keyword}

Content:
{content[:500]}
'''


from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.ui import Console
from autogen_core import CancellationToken
from autogen_ext.models.openai import OpenAIChatCompletionClient

import os
from dotenv import load_dotenv

load_dotenv()


model_client = OpenAIChatCompletionClient(
    model=os.getenv("OPENAI_MODEL"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

agent = AssistantAgent(
    name="keytrace_agent",
    model_client=model_client,
    system_message=prompt,
)

msg = TextMessage(content=prompt, source="user")

print("msg:", str(msg))


asyncio.run(run_assistant(msg))

