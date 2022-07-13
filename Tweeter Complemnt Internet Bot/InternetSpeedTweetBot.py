from selenium import webdriver
from time import sleep

TWEETER_EMAIL = "test71747478@gmail.com"
TWEETER_PASS = "71747478"
GOOGLE_DRIVER = "C:/Devolopment/chromedriver.exe"
PROMISED_UP = 50
PROMISED_DOWN = 10


class Bot:
    def __init__(self):
        self.__driver = webdriver.Chrome(GOOGLE_DRIVER)
        self.__up = 0
        self.__down = 0

    def get_internet_speed(self):
        self.__driver.get("https://www.speedtest.net/")
        sleep(10)
        go_button = self.__driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                        '1]/a')
        go_button.click()
        sleep(30)
        download_span = self.__driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
            '2]/div/div[2]/span')
        self.__up = float(download_span.text)
        sleep(15)
        upload_span = self.__driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
            '3]/div/div[2]/span')
        self.__down = float(upload_span.text)

    def get_up(self):
        return self.__up

    def get_down(self):
        return self.__down

    def tweet_at_provider(self):
        self.__driver.get("https://twitter.com/?logout=1617742918494")
        sleep(10)
        login_button = self.__driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]')
        login_button.click()
        sleep(5)
        email_input = self.__driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        email_input.click()
        email_input.send_keys(TWEETER_EMAIL)
        sleep(5)
        pass_input = self.__driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        pass_input.click()
        pass_input.send_keys(TWEETER_PASS)
        sleep(3)
        done_button = self.__driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
        done_button.click()
        sleep(3)
        tweet_label = self.__driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div['
            '2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet_label.click()
        sleep(3)
        msg = f"Hey Internet provider\nWhy is my Internet speed {self.__down}:down/{self.__up}:up\n" \
              f"When I pay for {PROMISED_DOWN}:down/{PROMISED_UP}:up ?! "
        tweet_label.send_keys(msg)
        sleep(3)
        tweet_button = self.__driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div['
            '2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()
        sleep(3)

    def close_web_driver(self):
        self.__driver.close()
