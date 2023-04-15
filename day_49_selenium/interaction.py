from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service = Service("C:\ChromeWebDriver\chromedriver.exe")
driver = webdriver.Chrome(service=service)
chrome_driver_path = "D:\Development\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

art_num = driver.find_element(By.ID, "articlecount")
print(art_num.text)






driver.quit()