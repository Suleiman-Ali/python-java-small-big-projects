from bs4 import BeautifulSoup
import requests
import smtplib
from email.message import EmailMessage

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
ACCEPT = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
URL = "https://www.amazon.com.tr/HyperX-Origins-Mekanik-Gaming-HX-KB7RDX-US/dp/B07YMHGP86/ref=sr_1_5?dchild=1&qid=1617138020&s=videogames&sr=1-5"
headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": USER_AGENT
}
response = requests.get(url=URL, headers=headers)
data = response.text
response.raise_for_status()
soup = BeautifulSoup(data, "html.parser")
price_lines = soup.find("div", class_="a-section a-spacing-small")
price_line = price_lines.find("span", class_="a-size-medium a-color-price priceBlockSalePriceString")
price_list = price_line.string.split("₺")[1].split(",")[0].split(".")
price = int(price_list[0] + price_list[1])
needed_price = 2000
if price < needed_price:
    msg = EmailMessage()
    head_of_msg = f"Price is now below {needed_price} You can go to the link and buy the product now:\n"
    body_of_msg = URL
    whole_msg = head_of_msg + body_of_msg
    msg.set_content(whole_msg)
    msg["Subject"] = f"Amazon Tracker Bot -> product now below {needed_price}"
    msg["From"] = "test71747478@gmail.com"
    msg["To"] = "alkengjooba@gmail.com"
    with smtplib.SMTP("smtp.gmail.com", timeout=60, port=587) as connection:
        connection.starttls()
        connection.login(user="test71747478@gmail.com", password="71747478")
        connection.send_message(msg)



