import bs4
import requests

# Web scraping
# Site which i want to scrape from
result = requests.get("https://cs.wikipedia.org/wiki/Hlavn%C3%AD_strana")
# print(result.text)
soup = bs4.BeautifulSoup(result.text, "lxml")


# print(soup)
print(soup.select('title')[0].get_text())
print(soup.select('h1')[0].get_text())

# This will get me every p tags text on a page
paragraphs = soup.select('p')
x = 0
for _ in range(len(paragraphs)):
    print(soup.select('p')[x].getText())
    x += 1

images = (soup.select('.image'))
# here [src], [srcset] should grab the link for download but it does not
print(images)
# image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')
# f = open('my_new_file_name.jpg','wb')
# f.write(image_link.content)
# f.close()


base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

# res = requests.get(base_url.format('1'))
# soup = bs4.BeautifulSoup(res.text, "lxml")
# print(soup.select(".product_pod"))
# products = soup.select(".product_pod")
two_star_titles = []

for n in range(1, 51):

    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, "lxml")
    books = soup.select(".product_pod")

    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            two_star_titles.append(book.select('a')[1]['title'])

print(two_star_titles)
