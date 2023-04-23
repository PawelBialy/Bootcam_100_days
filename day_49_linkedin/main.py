from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
service = Service("D:\Development\chromedriver.exe")

# create Options object with detach option
options = Options()
options.add_experimental_option("detach", True)

#navigate to linkedin
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
URL = "https://www.linkedin.com/jobs/search/?currentJobId=3574827350&distance=25&geoId=105072130&keywords=Python%20Developer&refresh=true"
# login and password
user= "alleckey96@gmail.com"
user_password = "Komputronikpl12"

driver.get(URL)
#dojście do okna logowania
log_in = driver.find_element(By.LINK_TEXT, "Zaloguj się")
time.sleep(3)
log_in.click()

#logowanie

login = driver.find_element(By.ID, "username")
login.send_keys(user)

password = driver.find_element(By.ID, "password")
password.send_keys(user_password)
password.send_keys(Keys.ENTER)