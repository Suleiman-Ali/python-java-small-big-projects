import requests
from datetime import datetime as dt
from email.message import EmailMessage
import smtplib
import time

MY_LAT = 40.775711
MY_LONG = 30.400780


def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    data = iss_response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    if ((MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5)) and ((MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5)):
        return True


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = dt.now().hour
    if sunset <= time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_dark():
        my_email = "test71747478@gmail.com"
        password = "71747478"
        msg = EmailMessage()
        msg.set_content("Look up the ISS is currently in the sky!")
        msg["Subject"] = "ISS IN THE SKY 😊 "
        msg["From"] = my_email
        msg["To"] = "alkengjooba@gmail.com"
        with smtplib.SMTP("smtp.gmail.com", port=587, timeout=60) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.send_message(msg)
