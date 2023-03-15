import requests
from datetime import datetime
sheety_endpoint = "https://api.sheety.co/cd4cdf720a554ac4e1919d9c8297a553/copyOfFlightDeals/prices"
kiwi_api_key = "jej1fyqMl6dFbbnQasBMtbpwdxXtAc0R"
kiwi_endpoint = "https://api.tequila.kiwi.com"


cities = ["Rzeszów","Sydney","Istambul","Kuala Lumpur","New York","San Francisco","Cape Town","Krakow"]
header = {"apikey": kiwi_api_key,}
#
for city in cities:
    location = {
        "term": city,
        "location_types": "airport",
        "active_only" : "true",
        "sort": "rank",
    }
    response = requests.get(url=f"{kiwi_endpoint}/locations/query", params=location, headers=header )
    data = response.json()
    iata_code = data["locations"][0]["id"] # that's my list of iataCode for next step in challenge.
    print(f"IATA code for {city} is {iata_code}.")




# sheet_inputs = {
#     "price" : {
#     "city": "Lubaczow" ,
#     "iataCode" : "LUB",
#     "lowestPrice" : 100,
#     }
# }

# sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=bearer_headers)

# bearer_headers = {
#     "Authorization": "Bearer qwertyuiasdfghj",
# }

# sheet_response = requests.get(url=sheety_endpoint, headers=bearer_headers)
# print(sheet_response.json())
# prices = sheet_response.json()["prices"]
# price2 = prices[2]
# price2["iataCode"] = "TESTING2"
# new_price = {
#     "price" : price2
# }
#
# new_price2 = {
#     "price" : {
#         "iataCode": ''
#     }
# }
#
# for row in range (2,13):
#     sheet_response = requests.put(url=f"{sheety_endpoint}/{row}", json=new_price2, headers=bearer_headers)
# print(price2)
# print(f"{sheety_endpoint}/2")
# print(sheet_response)
#















# def find_lub(price):
#   return price ["city"] == "Lubaczow"
# lubaczow = list(filter(find_lub, prices))
# print(lubaczow[0]["iataCode"])