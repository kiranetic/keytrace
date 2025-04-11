import asyncio
from crawl4ai import AsyncWebCrawler

async def crawl_scrap(url):
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url)
        return result.markdown

def crawl_init(url):
    result = asyncio.run(crawl_scrap(url))
    return result
