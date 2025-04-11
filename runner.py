from agents import extraction_agent
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken

async def run_agent(prompt) -> str:
    agent = extraction_agent()
    message = TextMessage(content=prompt, source="user")

    response = await agent.on_messages(
        [message],
        cancellation_token=CancellationToken(),
    )

    return response.chat_message.content

