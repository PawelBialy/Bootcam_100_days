import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = Service("D:\Development\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=CHROME_DRIVER_PATH, )
# #Twitter for study account details
TWITTER_EMAIL = "alleckey96@gmail.com"
TWITTER_PASSWORD = "Uczsieciulu1"
PROMISED_DOWN = 100
PROMISED_UP = 300

#Internet Speed Class

class InternetSpeedTwitterBot:

    def __init__(self, driver):
        self.up = 0
        self.down = 0
        self.driver = webdriver.Chrome(service=CHROME_DRIVER_PATH)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        accept_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        accept_button.click()
        time.sleep(3)
        click_start = self.driver.find_element(By.CSS_SELECTOR, ".start-text")
        click_start.click()
        time.sleep(45)
        self.up = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    #     # print(speed_up)
    #     # print(speed_down)

#Twitter at provider

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(2)
        email = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet_compose = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)
        tweet_button = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()
        time.sleep(2)
        self.driver.quit()

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()