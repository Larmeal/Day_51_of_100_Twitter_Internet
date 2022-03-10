from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time


dotenv_path = Path(".env")
load_dotenv(dotenv_path=dotenv_path)

USER = os.getenv("GMAIL")
PASSWORD = os.getenv("PASSWORD")
PHONE = os.getenv("PHONE")

PROMISED_DOWN = 1000
PROMISED_UP = 100
CHROME_DRIVER = "C:\Developer\chromedriver.exe"
TWITTER = "https://twitter.com/?logout=1646895933718"
INTERNET_SPEED_CHECK = "https://fast.com/#"

class InternetSpeedTwitterBot:

    def __init__(self, path_driver_chrome): 
        self.driver = webdriver.Chrome(executable_path=path_driver_chrome)
        self.up = 0
        self.down = 0

    def get_internet_speed(self, web_browser):
        self.driver.get(web_browser)
        self.driver.maximize_window()

        time.sleep(15)
        self.test_internet = self.driver.find_element_by_xpath('//*[@id="show-more-details-link"]')
        self.test_internet.click()
        time.sleep(50)
        self.down = float(self.driver.find_element_by_xpath('//*[@id="speed-value"]').text)
        self.up = float(self.driver.find_element_by_xpath('//*[@id="upload-value"]').text)

    def tweet_at_provider(self, web_browser):
        self.driver.get(web_browser)
        self.driver.maximize_window()
        time.sleep(5)
        self.log_in_twit = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
        self.log_in_twit.click()

        time.sleep(2)
        self.user = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
        self.user.send_keys(USER)
        self.user.send_keys(Keys.ENTER)

        time.sleep(2)
        self.password = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/label/div/div[2]/div/input')
        self.password.send_keys(PHONE)
        self.password.send_keys(Keys.ENTER)

        time.sleep(2)
        self.password = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        self.password.send_keys(PASSWORD)
        self.password.send_keys(Keys.ENTER)

        time.sleep(5)
        self.ready_write = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        self.ready_write.click()

        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            self.content = f"""Hey Internet Provider, why is my internet speed {int(self.down)} download / {int(self.up)} upload when I pay for {PROMISED_DOWN} download / {PROMISED_UP} upload?"""
            self.write = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div/span/br')
            self.write.send_keys(self.content)

            time.sleep(2)
            self.twit = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
            self.twit.click()
            self.driver.quit()

        else:
            self.driver.quit()


bot_twitter = InternetSpeedTwitterBot(CHROME_DRIVER)
bot_twitter.get_internet_speed(INTERNET_SPEED_CHECK)
bot_twitter.tweet_at_provider(TWITTER)