import asyncio
from crawler import crawler
from utils import prompt_builder
from agents import extraction_agent
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken


async def main():
    url = "https://www.gov.uk/send-prisoner-money"
    keyword = "bank transfer"

    print(f"🕸️ Crawling: {url}")
    content = await crawler(url)

    if not content:
        print("❌ No content extracted from the page.")
        return

    prompt = prompt_builder(content, keyword)
    print("🧠 Prompt ready. Sending to agent...")

    agent = extraction_agent()
    message = TextMessage(content=prompt, source="user")

    response = await agent.on_messages(
        [message],
        cancellation_token=CancellationToken(),
    )
    print("\nresponse.chat_message.content", response.chat_message.content)
    print("\nresponse.inner_messages", response.inner_messages)
    print("\nresponse.chat_message", response.chat_message)


if __name__=="__main__":
    asyncio.run(main())

