from crawler import crawler
from utils import prompt_builder
import asyncio

async def main():
    url = "https://www.gov.uk/send-prisoner-money"
    keyword = "bank transfer"

    print(f"Crawling: {url}")
    content = await crawler(url)

    prompt = prompt_builder(content, keyword)

    print("Prompt", prompt)


if __name__=="__main__":
    asyncio.run(main())

