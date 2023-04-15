from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:\ChromeWebDriver\chromedriver.exe")
driver = webdriver.Chrome(service=service)

chrome_driver_path = "D:\Development\chromedriver.exe"


driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.python.org/")


event_time = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# for time in event_time:
#     print(time.text)

name_event = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")


# for event in name_event:
#     print(event.text)
events = {}

for n in range (len(event_time)):
    events[n] = {
        "time":event_time[n].text,
        "name": name_event[n].text,

    }

print(events)










# price = driver.find_element(By.NAME, "q")
# print(price.get_attribute("placeholder"))

#

# documentation = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation.text)

# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print ( bug_link.text)
driver.quit()