from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

web_driver = "C:/Devolopment/chromedriver.exe"
driver = Chrome(web_driver)
driver.get("https://tinder.com/app/recs")
login = driver.find_element_by_xpath(
    '//*[@id="t--942482051"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
login.click()
time.sleep(3)
# login with facebook
facebook_button = driver.find_element_by_xpath('//*[@id="t-1312279441"]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook_button.click()
time.sleep(3)
windows = driver.window_handles
facebook_window = windows[1]
driver.switch_to.window(facebook_window)
user = driver.find_element_by_xpath('//*[@id="email"]')
user.send_keys("test71747478@gmail.com")
password = driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys("20032003")
time.sleep(1)
log_in_face_book_button = driver.find_element_by_xpath('//*[@id="loginbutton"]')
log_in_face_book_button.click()
time.sleep(1)
driver.switch_to.window(windows[0])
time.sleep(10)
allow = driver.find_element_by_xpath('//*[@id="t-1312279441"]/div/div/div/div/div[3]/button[1]')
allow.click()
time.sleep(1)
not_interssted = driver.find_element_by_xpath('//*[@id="t-1312279441"]/div/div/div/div/div[3]/button[2]')
not_interssted.click()
time.sleep(1)
agree = driver.find_element_by_xpath('//*[@id="t--942482051"]/div/div[2]/div/div/div[1]/button')
agree.click()
time.sleep(5)
pop_up = driver.find_element_by_xpath('//*[@id="t-1312279441"]/div/div/div[1]/button')
pop_up.click()
time.sleep(10)
while True:
    try:
        x = driver.find_element_by_xpath('//*[@id="t--942482051"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]')
        x.click()
        time.sleep(2)
    except NoSuchElementException:
        continue
