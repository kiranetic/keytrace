from crawler import crawl_init

url = "https://www.gov.uk/government/news/revised-guidance-when-applying-for-prior-authority"

content = crawl_init(url)

print(content)
