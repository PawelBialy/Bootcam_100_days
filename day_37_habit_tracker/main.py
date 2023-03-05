#advanced authentication and POST/PUT/ DELETE Requests

import requests
from datetime import  datetime
pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "pawelski"
TOKEN = "hjduwisja585qxndA"
GRAPH_ID = "graph1"
user_params = {
"token":"hjduwisja585qxndA",
"username": "pawelski",
"agreeTermsOfService": "yes",
"notMinor" : "yes",
}


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#  "id" : GRAPH_ID,
#  "name": "reading",
#  "unit": "page",
#  "type": "int",
#  "color": "sora",
# }
headers = {
 "X-USER-TOKEN" : TOKEN,
}
#

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers )
# print(response.text)

newpixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2023, month=3, day=4)
# print (today)

new_pixel_data = {
 "date": today.strftime("%Y%m%d"),
 "quantity": "1001",
}

# response = requests.post(url=newpixel_endpoint, json=new_pixel_data , headers=headers)
# print(response.text)

update_endpoint = f"{newpixel_endpoint}/{today.strftime('%Y%m%d')}"

update_pixel = {
 "quantity": "1010"

}

# response = requests.put(url=update_endpoint,json=update_pixel, headers=headers)
# print(response.text)

# delete_endpoint = f"{update_endpoint}"

response = requests.delete(url=update_endpoint, json=update_pixel, headers=headers)
print(response.text)