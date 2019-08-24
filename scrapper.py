import requests
from bs4 import BeautifulSoup
URL = 'https://www.amazon.de/Dell-Alienware-15-R4-Festplatte/dp/B07D5TM1QK/ref=sr_1_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=alienware+laptop&qid=1566632631&s=gateway&sr=8-1'

headers = {"User-Agents": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle")

print(title)
