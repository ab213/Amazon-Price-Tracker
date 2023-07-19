import requests
from bs4 import BeautifulSoup
import smtplib
def send_mail():
    #X is a SMTP number
    server=smtplib.SMTP('smtp.gmail.com'X)
    server.ehlo()
    server.starttls()
    server.ehlo()
    #enter your email ID and password
    server.login('xxx@gmail.com','Password')

    subject= "Price of the Product is down "
    body="Buy the prodcut as soon as possible, here is the link https://www.amazon.com/Wilson-Tour-Slam-Tennis-Racket/dp/B01C2MTHVG/ref=sr_1_5?crid=2OZW6LT4MXZI4&keywords=tennis+racket&qid=1689738731&sprefix=tennis+r%2Caps%2C309&sr=8-5)"
    msg= f"Subject: (subject)\n\n(body)"
    server.sendmail(
        "xxx@gmail.com",
        msg
    )
    print("Email has been sent ")
    server.quit()


URL= "https://www.amazon.com/Wilson-Tour-Slam-Tennis-Racket/dp/B01C2MTHVG/ref=sr_1_5?crid=2OZW6LT4MXZI4&keywords=tennis+racket&qid=1689738731&sprefix=tennis+r%2Caps%2C309&sr=8-5"

headers= {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"}
def check_price():
    page=requests.get(URL, headers=headers)

    soup=BeautifulSoup(page.content, 'html.parser')

    title=soup.find(id="productTitle").get_text()

    price=soup.find(id="priceblock_ourprice").get_text()

    converted_price=price[0:5]

    if converted_price<34:
        send_mail()

    print(title.strip())

