def prompt_builder(content, keyword):
    prompt = (
f'''
You are a helpful keyword scrapper assistant. 
From the provided web content, extract a sentence that is either directly about the given keyword or closely related/relevent to it. 
Don't rephrase or mention things not discussed in the content.
Strictly base your response on the content.

Keyword: {keyword}

Content:
{content}
'''
    )

    return prompt
