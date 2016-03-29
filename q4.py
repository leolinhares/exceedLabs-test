# Instale a biblioteca BeautifulSoup utilizando: pip install beautifulsoup4
# Execute usando python3 q4.py

# A biblioteca BeautifulSoup foi utilizada para facilitar a procura dos elementos
# HTML da pagina.

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

request = Request('http://www.submarino.com.br', headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(request).read()

soup = BeautifulSoup(page, 'html.parser')
l = soup.find(id="mais-vendidos")
price = l.find(class_="product-price-integer").get_text()
name = l.find(class_="productInfo").find("span").get_text()

print(name)
print(price)
