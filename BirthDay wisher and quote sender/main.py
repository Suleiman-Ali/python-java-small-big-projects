import datetime as dt
import pandas as pd
import random as rd
import smtplib
from email.message import EmailMessage

now = dt.datetime.now()
today_tuple = (now.month, now.day)
data = pd.read_csv("birthdays.csv")
birth_days_dict = {(data_row["month"] , data_row["day"]): data_row for (index, data_row) in data.iterrows() }

for i in birth_days_dict.values():
    my_email = "test71747478@gmail.com"
    password = "71747478"

    with open("quotes.txt", "r") as data:
        list = [i.strip('\n') for i in data.readlines()]
        qutoe = rd.choice(list)
        msg = EmailMessage()
        msg.set_content(qutoe)
        msg["Subject"] = "سليمان العلي: صباح الخير❤"
        msg["From"] = my_email
        msg["To"] = i["email"]

        with smtplib.SMTP("smtp.gmail.com", timeout=60, port=587) as connect:
            connect.starttls()
            connect.login(user=my_email, password=password)
            connect.send_message(msg)

if today_tuple in birth_days_dict:
    person = birth_days_dict[today_tuple]
    file_path = f"letter_{rd.randint(1,3)}.txt"
    with open(file_path, "r") as letter_data:
        letter = letter_data.read()
        new_letter = letter.replace('[NAME]', person["name"] )

    with smtplib.SMTP("smtp.gmail.com", timeout=60, port=587) as connection:
            my_email = "test71747478"
            receiver = person["email"]
            massage = EmailMessage()
            massage.set_content(new_letter)
            massage["Subject"] = "Happy Birth Day!"
            massage["From"] = my_email
            massage["To"] = receiver
            connection.starttls()
            connection.login(my_email,71747478)
            connection.send_message(massage)





