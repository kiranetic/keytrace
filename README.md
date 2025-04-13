# Keytrace: Smart web content extractor powered by LLMs  

Keytrace is a lightweight, intelligent tool that scrapes web pages and extracts keyword-relevant sentences using LLMs. Designed to be efficient, simple, and accurate — perfect for quick analysis, audits, or knowledge extraction tasks.

 <br>

## 📌 Overview

Keytrace is a lightweight, LLM-powered content extraction assistant that:

- Crawls one or more web pages.
- Extracts clean, relevant content.
- Uses an LLM agent to locate **exact sentence-level matches** for a list of keywords.
- Outputs the results in a tabular format and exports them to a CSV.

It combines [crawl4ai](https://docs.crawl4ai.com/) for intelligent content scraping with [autogen-agentchat](https://microsoft.github.io/autogen/stable/) for conversational keyword extraction via OpenAI.

 <br>

## 🧠 Use Cases

- 📄 Legal/Policy document scanning  
- 📚 Research data collection  
- 🧹 Content audit / keyword validation  
- 📰 News or blog intelligence
- 📊 Extracting key messages from product or service websites

 <br>

## ⚙️ Features

- [x] Intelligent web content scraping
- [x] Precise, sentence-level keyword extraction 
- [x] URL + keyword inputs via simple `.txt` files
- [x] CSV export for reporting and automation
- [x] Built-in content pruning to remove noisy HTML
- [x] Clean tabular CLI display

 <br>

## 📁 Project Structure

```
keytrace/
├── agents.py           # LLM agent setup using AutoGen
├── crawler.py          # Web scraping using crawl4ai
├── runner.py           # Executes the agent
├── utils.py            # Prompt builder, table display, and CSV
├── main.py             # Main script / entry-point
├── patch.py            # Monkey patch for crawl4ai bug
├── input/
│   ├── urls.txt        # Input list of URLs to scrape
│   └── keywords.txt    # Input list of keywords to search
├── .env.sample         # Sample environment vars
├── requirements.txt    # Dependencies
└── README.md           # You're here!
```

 <br>

## 🚀 Getting Started

> ✅ Requires: Python 3.10+

### 1. Clone the repository
```bash
git clone https://github.com/kiranetic/keytrace.git
cd keytrace
```

### 2. Set up the virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -U -r requirements.txt
```

### 4. Configure environment variables
Copy the sample and edit:
```bash
cp .env.sample .env
```

Edit `.env`:
```
OPENAI_MODEL="gpt-4o-mini"         # or gpt-4, gpt-3.5-turbo, etc.
OPENAI_API_KEY="your-api-key"      # Add your OpenAI API key
```

### 5. Run crawl4ai setup
```bash
crawl4ai-setup          # Post-installation setup
crawl4ai-doctor         # Verify installation
```

### 6. Prepare input files

Edit the following input files in the `input/` directory:

1. `input/urls.txt`
    ```txt
    https://example.com/page-1
    https://example.com/page-2
    ```

2. `input/keywords.txt`
    ```
    climate
    carbon
    ```

### 7. Run the script

```bash
python3 main.py
```

The tool will:

1. Crawl each URL.
2. Extract and clean relevant content.
3. Ask the LLM agent to find sentence matches for each keyword.
4. Display the table in terminal and store in `output/data.csv`.

 <br>

## 📊 Example Output

```txt
Extracted Result Table:
url                           keyword          content
https://example.com/page-1    climate          Climate change is a major concern.
https://example.com/page-1    carbon           The new carbon tax policy takes effect this year.
...
```

 <br>

## 🎓 Project Background  

This project was originally built as part of a technical assignment:  

**Problem Statement**:  <br>
Develop a Python script leveraging Autogen v0.4, OpenAI and LLM that takes a list of URLs and a list of keywords as input and scrape the content of each URL and extract information related to the keywords (e.g., the sentence or paragraph where it appears).  

**URLs to scrape information**:  <br>
https://www.gov.uk/government/news/revised-guidance-when-applying-for-prior-authority  <br>
https://www.gov.uk/government/news/local-heritage-to-be-protected-with-20-million-offunding  

**Keywords to search in the links**:  
- Landfill Tax  
- Solid waste  

**Sample Output**:  
| Link | Keyword | Content |
| ---- | ------- | ------- |
| https://www.gov.uk/government/news/revisedguidance-when-applyingfor-prior-authority | Landfill Tax | UK's new garbage tax formula is under review due to concerns over its fairness and impact on citizens |
| https://www.gov.uk/government/news/local-heritageto-be-protected-with-20-million-of-funding | Concrete | Researchers have developed a groundbreaking carboncapturing concrete using seawater and CO2, offering a sustainable alternative for construction |

**References**:  
1. [AutoGen — AutoGen](https://microsoft.github.io/autogen/stable/)  
2. [What is AutoGen?](https://www.youtube.com/watch?v=tBJarQyoPrM)  

 <br>

## 🤝 Collaboration

Keytrace is **open for feedback, collaboration, and extension**.  
Licensing will be added later.  
Feel free to fork, experiment, or reach out.

