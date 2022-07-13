import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from time import sleep

web_driver = "C:/Devolopment/chromedriver.exe"
form = "https://docs.google.com/forms/d/e/1FAIpQLScED3ba9D6xhsvTHt0Bz-rgGL013LL9DkQJZqG1hXFpiubIqw/viewform?usp=sf_link"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15",
    "Accept-Language": "en-US"
}
Url = "https://www.zillow.com/san-francisco-ca/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55905331176511%2C%22east%22%3A-122.33714196429393%2C%22south%22%3A37.68781406853905%2C%22north%22%3A37.8294264787927%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A359314%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A1200%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

response = requests.get(Url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
data = soup.find(class_="photo-cards photo-cards_wow photo-cards_short")
d_prices = data.findAll(class_="list-card-price")
adds = data.find_all("a")
#Data
prices = [i.text for i in d_prices]
address = [i.text for i in adds]
links = [i.get("href") for i in adds]
address = [address[i] for i in range(0, len(address), 2)]

driver = Chrome(web_driver)
for i in range(10):
    sleep(3)
    driver.get(form)
    sleep(5)
    add_input = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    add_input.click()
    add_input.send_keys(address[i])
    sleep(1)
    price_input = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.click()
    price_input.send_keys(prices[i])
    sleep(1)
    link_input = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.click()
    link_input.send_keys(links[i])
    sleep(1)
    send = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    send.click()







