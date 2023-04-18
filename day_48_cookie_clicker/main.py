from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
service = Service("D:\Development\chromedriver.exe")

# create Options object with detach option
options = Options()
options.add_experimental_option("detach", True)

# navigate to cookie clicker game
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")


timeout = time.time() + 5
five_min = time.time() + 60 * 5

while True:
    cookie.click()

    if time.time() > timeout:
        # get current money
        money = driver.find_element(By.ID, "money").text
        if "," in money:
            current_money = int(money.replace(",", ""))
        else:
            current_money = int(money)

        # buy tool
        store = driver.find_elements(By.CSS_SELECTOR, "#store b")
        for upgrade in store[::-1]:
            upgrade_text = upgrade.text
            if upgrade_text != "":
                detail = upgrade_text.split("-")
                product = detail[0].strip()
                cost = detail[-1].strip()
                if "," in cost:
                    cost = cost.replace(",", "")
                cost_int = int(cost)
                if current_money >= cost_int:
                    driver.find_element(By.ID, f"buy{product}").click()
                    break
                else:
                    continue

        timeout = time.time() + 10

    if time.time() > five_min:
        cookie_per = driver.find_element(By.ID, "cps").text
        print(cookie_per)
        break




























# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import time
# service = Service("D:\Development\chromedriver.exe")
#
# # create Options object with detach option
# options = Options()
# options.add_experimental_option("detach", True)
#
# # navigate to cookie clicker game
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=service, options=options)
# driver.get("https://orteil.dashnet.org/experiments/cookie/")
#
#
# #find cookie to click on it
# cookie = driver.find_element(By.ID, "cookie")
#
# #upgrade ids
#
# items = driver.find_elements(By.CSS_SELECTOR, "#store div")
# item_ids = [item.get_attribute("id") for item in items]
#
#
# timeout = time.time() + 2
# five_min = time.time() + 60*0.5 # 5minutes
#
# while True:
#     cookie.click()
#
#     if time.time() > timeout:
#         #find all prices
#         all_prices = driver.find_elements(By.ID, "store b")
#         item_prices = []
#
#
#         #convert b text to integer
#
#         for price in all_prices:
#             element_text = price.text
#             if element_text != "":
#                 cost = int(element_text.split("-")[1].strip().replace(",", ""))
#                 item_prices.append(cost)
#             # Create dictionary of store items and prices
#         cookie_upgrades = {}
#         for n in range(len(item_prices)):
#             cookie_upgrades[item_prices[n]] = item_ids[n]
#
#         #get current cookie count
#         money_element = driver.find_element(By.ID, "money").text
#         if "," in money_element:
#             money_element = money_element.replace(",","")
#         cookie_count = int(money_element)
#
#         # Find upgrades that we can currently afford
#         affordable_upgrades = {}
#         for cost, id in cookie_upgrades.items():
#             if cookie_count > cost:
#                 affordable_upgrades[cost] = id
#
#             if affordable_upgrades:
#                 # Purchase the most expensive affordable upgrade
#                 print(affordable_upgrades)
#                 highest_price_affordable_upgrade = max(affordable_upgrades)
#                 to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
#                 driver.find_element(By.CLASS_NAME, "grayed").click()
#                 # Update affordable_upgrades list
#                 del affordable_upgrades[highest_price_affordable_upgrade]
#
#
#
#         #Add another 5 seconds until the next check
#         timeout = time.time() + 5
#
#     if time.time() > five_min:
#         cookie_per_s = driver.find_element(By.ID,"cps").text
#         print(cookie_per_s)
#         break
#
#
#
#




















