
import requests 
from  selenium import webdriver
from bs4 import BeautifulSoup
import smtplib
import time


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:77.0) Gecko/20100101 Firefox/77.0'}

url = ''
target_price = ''

def check_price():
	options = webdriver.ChromeOptions()

	options.add_argument('--incognito')
	options.add_argument('--headless')
	options.add_argument('--disable-extensions')
	options.add_argument('start-maximized')
	options.add_argument('disable-infobars')
	    
	browserdriver = webdriver.Chrome(chrome_options=options, executable_path=r'')

	browserdriver.get(url)

	content = browserdriver.page_source

	soup = BeautifulSoup(content, 'lxml')

	title = soup.find(id="productTitle").get_text()

	price = soup.find(id="priceblock_ourprice").get_text()

	converted_price = float(price[1:5])

	print(title.strip())
	print(converted_price)

	if converted_price < target_price:
		send_mail()

def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('', '')

	subject = 'Price Change'
	body = 'Check the Amazon link: '+url

	msg = f"Subject: {subject}\n\n{body}"

	server.sendmail(
		'',
		'',
		msg
		)

	server.quit()

while(True): 
	check_price()
	time.sleep(3600)


