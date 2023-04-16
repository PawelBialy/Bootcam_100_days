from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
service = Service("D:\Development\chromedriver.exe")

# create Options object with detach option
options = Options()
options.add_experimental_option("detach", True)

# navigate to cookie clicker game
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "reset")
print(cookie.text)





