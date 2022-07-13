import requests
from bs4 import BeautifulSoup
date = input("What year u wanna travel to?").split()
year = date[0]
month = date[1]
day = date[2]
URL = f"https://www.billboard.com/charts/hot-100/{year}-0{month}-{day}"
response = requests.get(url=URL)
data = response.text
soup = BeautifulSoup(data, "html.parser")
songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
songs_title = [song.string for song in songs]
