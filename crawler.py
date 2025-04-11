import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator


async def crawler(url):

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
            # print(f"Filtered markdown:\n{result.markdown.fit_markdown}")
            return result.markdown.fit_markdown
        else:
            print(f"Crawl failed:\n{result.error_message}")
            return None

