import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("D:\Development\chromedriver.exe")
#navigate to twitter
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)


e_mail = "alleckey96@gmail.com"
password_twitter = "Uczsieciulu1"


#get in speedtest website

speed_test = driver.get("https://www.speedtest.net/")

zgody = driver.find_element(By.ID, "onetrust-accept-btn-handler")
zgody.click()
click_start = driver.find_element(By.CSS_SELECTOR, ".start-text")
click_start.click()
time.sleep(60)

speed_up = driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text

speed_down = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

print(speed_up)
print(speed_down)