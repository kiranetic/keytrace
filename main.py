import asyncio
from crawler import crawler
from utils import prompt_builder
from agents import extraction_agent
from runner import run_agent


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

    extracted_text = await run_agent(prompt)

    print("Extracted text:", extracted_text)


if __name__=="__main__":
    asyncio.run(main())

