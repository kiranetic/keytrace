import csv
import os
from tabulate import tabulate


def prompt_builder(content, keyword_list):
    keywords = ", ".join(keyword_list)

    prompt = (
f"""
You are a smart extraction assistant.
Your task is to go through the provided content and extract **all exact sentences** that are directly or closely related/relevant to any of the given keywords.

- Extract only exact sentences as they appear in the content. No paraphrasing.
- If there are multiple matches for a keyword, return all of them.
- If a keyword is not found, skip it — no need to mention it.
- Format the output as JSON, like:

[
  {{
    "keyword": "example_keyword",
    "matches": [
      "Exact sentence 1.",
      "Exact sentence 2."
    ]
  }},
  ...
]

Here are the inputs:

Keywords: {keywords}

**Content:**
{content}
"""
    )

    return prompt.strip()


def extract_json_block(json_response):
    if "```json" in json_response:
        return json_response.split("```json")[-1].split("```")[0].strip()
    return json_response.strip()


def display_result(data_list):
    table = tabulate(data_list, headers="keys", tablefmt="plain", showindex="always")
    print(f"Extracted Result Table:\n{table}")
    return


def save_to_csv(data_list, file):
    headers = ["url", "keyword", "content"]

    output_dir = os.path.dirname(file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data_list)
        print(f"Table stored as CSV. Filename: {file}.")
    
    return
