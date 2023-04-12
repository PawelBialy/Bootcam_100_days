import lxml
import requests
from bs4 import BeautifulSoup
import smtplib
######################## Find price ##################
URL =  "https://www.amazon.com/dp/B08CF573K3/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0"


header = {
    "Accept-Language" : "en,en-US;q=0.9,pl-PL;q=0.8,pl;q=0.7",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
}


response = requests.get(URL, headers=header)
data = response.text

### Making soup and float price
soup = BeautifulSoup( data, "lxml" )
price = soup.find(class_="a-offscreen").get_text()
split_price = price.split("$")[1]
float_price = float(split_price)
# print(float_price)
##### Check, if price is lower than 100 and sending e-mail
passw = "vewsiwdobmsuqmde"
e_mail = "alleckey96@gmail.com"

price = 200

title = soup.find(id="productTitle").text


if price > float_price:
    message = f"Amazon promotion!\n {title} now just for {float_price} ! "
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=e_mail, password=passw)
        connection.sendmail(from_addr=e_mail,
                            to_addrs=e_mail,
                            msg=f"Subject: {message} \n\n  {URL} ")


