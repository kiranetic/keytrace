import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator


async def crawl_scrap(url):

    md_generator = DefaultMarkdownGenerator(
        content_filter=PruningContentFilter(threshold=0.5),
        options={"ignore_links": True}
    )

    config = CrawlerRunConfig(
        markdown_generator=md_generator
    )

    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url, config=config)

        if result.success:
            print("Filtered markdown:\n", result.markdown.fit_markdown)
            return result.markdown.fit_markdown
        else:
            print("Crawl failed:", result.error_message)
            return None


def crawl_init(url):
    result = asyncio.run(crawl_scrap(url))
    return result

crawl_init("https://www.asdgdiceds.uk/sen-prisoner-money")