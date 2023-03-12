import requests
# from pprint import pprint/
SHEETY_ENDPOINT = "https://api.sheety.co/cd4cdf720a554ac4e1919d9c8297a553/copyOfFlightDeals/prices"
class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT,)
        data = response.json()
        self.destination_data = data["prices"]
        #pprint (data)
        return self.destination_data

    def update_destination(self):
        for city in self.destination_data:
            new_data = {
                'price' : {
                "iataCode" : city["iataCode"]
            }
            }

            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}",json=new_data )
            print(response.text)