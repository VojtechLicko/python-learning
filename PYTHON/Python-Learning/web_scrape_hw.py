import bs4
import requests

result = requests.get("http://quotes.toscrape.com/")
soup = bs4.BeautifulSoup(result.text, "lxml")
# print(soup)
# u create new set with set()
all_authors = []
authors = soup.select(".author")
# All authors on page 1
for i, author in enumerate(authors):
    all_authors.append(soup.select(".author")[i].getText())

all_unique_authors = set(all_authors)
print(all_unique_authors)

all_quotes = []
quotes = soup.select(".text")
# all quotes on page 1
for i, quote in enumerate(quotes):
    all_quotes.append(soup.select(".text")[i].getText())

print(all_quotes)

# top ten tags
tags = soup.select(".tag-item")
for i, tag in enumerate(tags):
    print(soup.select(".tag-item")[i].get_text())

# all authors on all pages
authors_on_all_pages = []
quotes_url = "http://quotes.toscrape.com/page/{}/"
n = 0

while True:
    url = quotes_url.format(str(n))
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "lxml")
    for i, author in enumerate(soup.select(".author")):
        authors_on_all_pages.append(soup.select(".author")[i].getText())
    n += 1
    # print(authors_on_all_pages)
    if not soup.select(".next"):
        break

unique_authors_on_all_pages = set(authors_on_all_pages)
print(unique_authors_on_all_pages)
