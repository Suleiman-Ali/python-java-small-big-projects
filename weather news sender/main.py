import requests
from email.message import EmailMessage
import smtplib

api_key_not_mine = "69f04e4613056b159c2761a9d9e664d2"
my_api = "0109ea2fc428974dc31f639b9571d160"
my_lat = 40.775711
my_long = 30.400780

parameters = {
    "lat": my_lat,
    "lon":my_long,
    "appid":my_api,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
hourly_out = data["hourly"]
slice_12 = hourly_out[:12]
temps = []
for i in slice_12:
    temps.append(i['temp'])

temp_now =int(temps[0] - 273.15)
temp_6 = int(temps[5] - 273.15)
temp_12 = int(temps[11] - 273.15)

ides = []
for i in slice_12:
    ides.append(int(i["weather"][0]['id']))
result = 0
for i in range (len(ides)):
    result += ides[i]

f_result = result / len(ides)


r3d =   "الجو مو وزين في رعد برا خذي شمسيه. ☂️"
rzaz = "الجو برا رذاذ مطر يعني مو مطر كثير بس خذي شمسية☂️ الاحتياط واجب."
rain = "الجو مطر خذي شمسيه مشان ماتصيرين تسبحين. ☂️"
snow = "الجو برا ثلج ماتقليلي شمطلعك. ☂️ خذي شمسيه."
smoke = "الجو زين شويه بس في غلاف جوي مايلزم شمسيه خذي كمامه. 😷 "
good = "الجو حلو والسماء صافيه .. "
cloudy = "الجو مغيم بس حلو في احتمال انها تمطر خذي شمسيه. ☂️"

r3d_msg = r3d + "\n" + f"درجه الحراره حاليا: {temp_now}" + "\n" + f"درجه الحراره بعد 6 ساعات: {temp_6}" + "\n" + f"درجه الحراره بعد 12 ساعه : {temp_12}"
rzaz_msg = rzaz + "\n" + f"درجه الحراره حاليا: {temp_now}" + "\n" + f"درجه الحراره بعد 6 ساعات: {temp_6}" + "\n" + f"درجه الحراره بعد 12 ساعه : {temp_12}"
rain_msg = rain + "\n" + f"درجه الحراره حاليا: {temp_now}" + "\n" + f"درجه الحراره بعد 6 ساعات: {temp_6}" + "\n" + f"درجه الحراره بعد 12 ساعه : {temp_12}"
snow_msg = snow + "\n" + f"درجه الحراره حاليا: {temp_now}" + "\n" + f"درجه الحراره بعد 6 ساعات: {temp_6}" + "\n" + f"درجه الحراره بعد 12 ساعه : {temp_12}"
smoke_msg = smoke + "\n" + f"درجه الحراره حاليا: {temp_now}" + "\n" + f"درجه الحراره بعد 6 ساعات: {temp_6}" + "\n" + f"درجه الحراره بعد 12 ساعه : {temp_12}"
good_msg = good + "\n" + f"درجه الحراره حاليا: {temp_now}" + "\n" + f"درجه الحراره بعد 6 ساعات: {temp_6}" + "\n" + f"درجه الحراره بعد 12 ساعه : {temp_12}"
cloudy_msg = cloudy + "\n" + f"درجه الحراره حاليا: {temp_now}" + "\n" + f"درجه الحراره بعد 6 ساعات: {temp_6}" + "\n" + f"درجه الحراره بعد 12 ساعه : {temp_12}"
massage = EmailMessage()
my_email = "test71747478@gmail.com"
password = "71747478"
if ides[0] >= 200 and ides[0] < 300:
    massage.set_content(r3d_msg)

elif ides[0] >= 300 and ides[0] < 500:
    massage.set_content(rzaz_msg)

elif ides[0] >= 500 and ides[0] < 600:
    massage.set_content(rain_msg)

elif ides[0] >= 600 and ides[0] < 700:
    massage.set_content(snow_msg)

elif ides[0] >= 700 and ides[0] < 800:
    massage.set_content(smoke_msg)

elif ides[0] >= 800 and ides[0] < 825:
    massage.set_content(good_msg)

elif ides[0] >= 825:
    massage.set_content(cloudy_msg)
else:
    massage.set_content("الجو مو معروف للبرنامج 😑")

massage["Subject"] = "صباح الخير ياأمي ❤ الجو اليوم:"
massage["From"] = my_email
massage["To"] = "rajahedar1979@gmail.com"

with smtplib.SMTP("smtp.gmail.com", port=587, timeout=60) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.send_message(massage)




