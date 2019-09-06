import requests
from lxml import html
import smtplib  

#Method 1 of using this code

def sendMail():
	print("Function called")
	s = smtplib.SMTP('smtp.gmail.com', 587) 
	s.starttls() 
	s.login("senders_email", "password") 						#Your username and password for gmail using which you want to send the mail
	message = "Price Dropped Bro" 							#Feel free to change the message Dude
	s.sendmail("senders_email", "receivers_email", message) 	#Sender's Email (mentioned Above) and Receiver's Email (Email on which you want to get the message)
	s.quit()


def get_name_price(URL):
	headers = {"User-Agents": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'} #Your User Agent

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

#Change the URL according to your product  Mine is Dell-Alienware-Gaming-Laptop!!!!!
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

##################################################

# Uncomment this to get 2nd use of this script that is keep a constant check.

# SORRY Currently unavailable but surely I ll update it soon