import requests
from bs4 import BeautifulSoup
URL = 'https://www.amazon.in/Dell-Alienware-Ready-Gaming-Notebook/dp/B07D6CMJYS/ref=sr_1_3?crid=128LG608426NP&keywords=alienware+laptops&qid=1566634506&s=gateway&sprefix=Alienware%2Caps%2C407&sr=8-3'
headers = {"User-Agents": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
converted_price = price[0:13]

print(converted_price)
#print(price.strip())
