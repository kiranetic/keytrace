import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url="https://docs.crawl4ai.com/")

        print(result.markdown)

asyncio.run(main())
