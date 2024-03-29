import requests
from flight_data import FlightData

tequila_endpoint = "https://tequila-api.kiwi.com"
tequila_api_key = "jej1fyqMl6dFbbnQasBMtbpwdxXtAc0R"

class FlightSearch:
    def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working.
        location_endpoint = f"{tequila_endpoint}/locations/query"
        headers = {"apikey" : tequila_api_key}
        query = {"term" : city_name, "location_types":"city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city, from_time, to_time):
        headers = {"apikey": tequila_api_key}
        query= {
            "fly_from": origin_city_code,
            "fly_to": destination_city,
            "date_from":from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y")
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }