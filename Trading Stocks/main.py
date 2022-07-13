import requests
from email.message import EmailMessage
import smtplib

api_key_for_news = "5b7eb0456b2b47d09828e98c70cf6ec7"
NEWS_URL = "https://newsapi.org/v2/everything"
STOCK_URL = "https://www.alphavantage.co/query"

COMPANY_NAME = "Tesla Inc"
data = {
    "symbol": "TSLA",
    "datatype": "json",
    "function": "TIME_SERIES_DAILY",
    "apikey": "47Y9SANRFT78A0KR",
    "interval":"5min"
    }

response = requests.get(STOCK_URL, params=data)
response.raise_for_status()
data = response.json()
yesterday_closing_price = float(data["Time Series (Daily)"]["2021-03-19"]["4. close"])
day_before_yesterday_closing_price = float(data["Time Series (Daily)"]["2021-03-18"]["4. close"])
difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)
diff_percent = (difference / yesterday_closing_price) * 100
if diff_percent > 5:
    parameters = {
        'q': COMPANY_NAME,
        'pageSize': 3,
        'apiKey': api_key_for_news
    }
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=parameters)
    tsla_data = news_response.json()
    d = tsla_data['articles'][0:3]
    top_three_news_title = [i['title'] for i in d]
    top_three_news_des = [i['description'] for i in d]
    percentage = str(diff_percent)[0:4] + '%'
    msg = "Title: " + top_three_news_title[0] + "\n" + "Description: " + top_three_news_des[0] + "\n" + "Title: " + \
          top_three_news_title[1] + "\n" + "Description: " + top_three_news_des[1] + "\n" + "Title: " + \
          top_three_news_title[2] + "\n" + "Description: " + top_three_news_des[2]
    sine_up = "TSLA:" + "🔺" + percentage
    sine_down = "TSLA:" + "🔻" + percentage
    my_email = "test71747478@gmail.com"
    password = "71747478"
    email_msg = EmailMessage()
    subject = ""
    if yesterday_closing_price > day_before_yesterday_closing_price:
        subject = f"Trading Stocks: {sine_up}"
    elif day_before_yesterday_closing_price > yesterday_closing_price:
        subject = f"Trading Stocks:{sine_down}"
    email_msg["Subject"] = subject
    email_msg["From"] = my_email
    email_msg["To"] = "alkengjooba@gmail.com"
    email_msg.set_content(msg)

    with smtplib.SMTP("smtp.gmail.com", timeout=60, port=587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.send_message(msg=email_msg)







