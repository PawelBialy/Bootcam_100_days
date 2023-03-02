#API Keys, Authentication, Enviroment Variables, Sending SMS -> that's what i'll learning in today's lesson.

#API KEY
import requests
OCW_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "364b6f69594600d1b195126dc0cac7be"




weather_params = {
    "lat": 52.229675,
    "lon": 21.012230,
    "appid": api_key,
}



response = requests.get(OCW_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700 :
        will_rain = True
if will_rain:
    print("Bring un umbrella")
