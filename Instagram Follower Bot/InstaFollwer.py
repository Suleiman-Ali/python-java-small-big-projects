from selenium import webdriver
from time import sleep
from random import randint
Target = "wwe"
USER_NAME = "test71747478@gmail.com"
PASSWORD = "71747478"
Web_driver_path = "C:/Devolopment/chromedriver.exe"


class Bot:
    def __init__(self):
        self.__driver = webdriver.Chrome(Web_driver_path)

    def login(self):
        self.__driver.get("https://www.instagram.com/")
        sleep(10)
        email_input = self.__driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        email_input.click()
        email_input.send_keys(USER_NAME)
        sleep(5)
        password_input = self.__driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.click()
        password_input.send_keys(PASSWORD)
        sleep(5)
        done_button = self.__driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        done_button.click()
        sleep(5)
        not_save = self.__driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_save.click()
        sleep(5)
        not_now = self.__driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        not_now.click()
        sleep(5)

    def find_followers(self):
        search_bar = self.__driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_bar.send_keys(Target)
        sleep(5)
        account = self.__driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div['
                                                      '3]/div/div[2]/div/div[1]/a/div')
        account.click()
        sleep(5)
        followers_page = self.__driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section'
                                                             '/ul/li[2]/a')
        followers_page.click()
        sleep(5)

    def follow_people(self):
        bar = self.__driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        sleep(3)
        for i in range(5):
            num = randint(1, 3)
            sleep(num)
            self.__driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', bar)
        sleep(5)
        all_buttons = self.__driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            n = randint(3, 8)
            try:
                button.click()
            except Exception:
                cancel_button = self.__driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_button.click()
            finally:
                sleep(n)

    def close_bot(self):
        self.__driver.quit()
        self.__driver.close()




