import requests
from lxml import html
import smtplib  

def sendMail():
	print("Function called")
	s = smtplib.SMTP('smtp.gmail.com', 587) 
	s.starttls() 
	s.login("hack7jack@gmail.com", "downloadapp007") 
	message = "Price Dropped Bro"
	s.sendmail("hack7jack@gmail.com", "gupta7nitin@gmail.com", message) 
	s.quit()


def get_name_price(URL):
	headers = {"User-Agents": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

	page = requests.get(URL, headers=headers)

	doc = html.fromstring(page.content)
	name = doc.xpath('//h1[@id="title"]//text()')
	price = doc.xpath('//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()')

	name = ' '.join(''.join(name).split()) if name else None
	price = ' '.join(''.join(price).split()).strip() if price else None

	price = price[2:]

	return name, price
	
def price_alert(url, dest_price):
	name, price = get_name_price(url)

	price_val = float(price.replace(',',''))
	if (price_val < dest_price):
		sendMail()
	else:
		print ("SHIT: price of " + str(name) + " is Rs " + price)

	return True


URL = 'https://www.amazon.in/Dell-Alienware-Ready-Gaming-Notebook/dp/B07D6CMJYS/ref=sr_1_3?crid=128LG608426NP&keywords=alienware+laptops&qid=1566634506&s=gateway&sprefix=Alienware%2Caps%2C407&sr=8-3'
reply = True
i = 0
while reply:
	try:
		print (i),
		reply = not price_alert(URL, 200000)
	
	except Exception as e:
		print ("Failure to get price from Amazon, trying again")
		i += 1
