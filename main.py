import asyncio
import time
import pandas as pd
from pathlib import Path
from tabulate import tabulate

import patch
from crawler import crawler
from utils import prompt_builder
from agents import extraction_agent
from runner import run_agent


URL_FILE = "input/urls.txt"
KEYWORD_FILE = "input/keywords.txt"
OUTPUT_FILE = "output/data.csv"


def load_input():
    url_file_path = Path(URL_FILE)
    url_file_read = url_file_path.read_text(encoding="utf-8").strip()
    url_list = url_file_read.splitlines()

    keyword_file_read = Path(KEYWORD_FILE).read_text(encoding="utf-8").strip()
    keyword_list = keyword_file_read.splitlines()

    return url_list, keyword_list


async def keytrace_processing(url, keyword):
    # print(f"🕸️ Crawling: {url}")
    content = await crawler(url)

    # if not content:
    #     print("❌ No content extracted from the page.")
    #     return

    prompt = prompt_builder(content, keyword)
    # print("🧠 Prompt ready. Sending to agent...")

    extracted_text = await run_agent(prompt)

    # print("Extracted text:", extracted_text)

    result = {
        "url": url,
        "keyword": keyword,
        "content": extracted_text
    }

    # print(result)

    return result
    


async def main():
    url_list, keyword_list = load_input()
    result_list = []

    for url in url_list:
        for keyword in keyword_list:
            result = await keytrace_processing(url, keyword)
            result_list.append(result)
            await asyncio.sleep(2)

    print(result_list)

    df = pd.DataFrame(result_list)

    df.to_csv(OUTPUT_FILE, index=False)

    table = tabulate(df, headers="keys", tablefmt="grid", showindex=False)
    print(table)



    return


if __name__=="__main__":
    asyncio.run(main())

