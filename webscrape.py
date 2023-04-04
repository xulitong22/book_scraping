from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for i in range (1,4):
    url = f'https://books.toscrape.com/catalogue/page-{i}.html'
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html,'html.parser')
    ol = soup.find('ol')
    books = ol.find_all('article', class_='product_pod')

    for book in books:
        img = book.find('img')
        title = img.attrs['alt']
        price = book.find('p',class_="price_color").text
        print(title," ", price)

