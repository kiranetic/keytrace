import asyncio
import json

import patch
from crawler import crawler
from agents import extraction_agent
from runner import run_agent
from utils import prompt_builder, extract_json_block, display_result, save_to_csv


URL_FILE = "input/urls.txt"
KEYWORD_FILE = "input/keywords.txt"
OUTPUT_FILE = "output/data.csv"


def load_input():
    url_list = []
    with open(URL_FILE, "r", encoding="utf-8") as f:
        for line in f:
            cleaned_line = line.strip()
            if cleaned_line:
                url_list.append(cleaned_line)

    keyword_list = []
    with open(KEYWORD_FILE, "r", encoding="utf-8") as f:
        for line in f:
            cleaned_line = line.strip()
            if cleaned_line:
                keyword_list.append(cleaned_line)

    return url_list, keyword_list


async def keytrace_processing(url, keyword_list):
    # print(f"🕸️ Crawling: {url}")
    content = await crawler(url)

    # if not content:
    #     print("❌ No content extracted from the page.")
    #     return

    prompt = prompt_builder(content, keyword_list)
    # print("🧠 Prompt ready. Sending to agent...")

    agent_response = await run_agent(prompt)
    # print("Agent response:", agent_response)

    json_str = extract_json_block(agent_response)
    # print("Formatted JSON:", json_str)

    try:
        result_json = json.loads(json_str)
    except Exception as e:
        print("❌ Exception:", e)
        return []

    result = []
    for item in result_json:
        keyword = item.get("keyword", "").strip()
        matches = item.get("matches", [])

        for match in matches:
            cleaned_match = match.strip()
            if cleaned_match and cleaned_match.lower() != "none":
                json_item = {
                    "url": url,
                    "keyword": keyword,
                    "content": cleaned_match
                }
            result.append(json_item)

    return result
    

async def main():
    url_list, keyword_list = load_input()
    result_list = []

    for url in url_list:
        result = await keytrace_processing(url, keyword_list)
        result_list.extend(result)

    # print("Result:", result_list)

    if result_list:
        display_result(result_list)
        save_to_csv(result_list, OUTPUT_FILE)

    return


if __name__=="__main__":
    asyncio.run(main())

