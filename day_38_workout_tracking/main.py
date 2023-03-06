import requests
from datetime import datetime
APP_ID = "5c54c69e"
API_KEY = "05964196295c83702d923317d6988d3c"
GENDER = "male"
WEIGHT = 93
HEIGHT = 190
AGE = 27

excercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/7031520c67436ee53c3ac2e96e4c3a72/myWorkouts/workouts"


excercise_text = input("Tell me which excercice you did: ")

headers = {
"x-app-id" : APP_ID,
"x-app-key" : API_KEY,
}


excercise_params = {
    "query" : excercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT ,
    "age" : AGE,
}




response = requests.post(excercise_endpoint, json= excercise_params , headers=headers)
result = response.json()
# print(result)

today = datetime.now().strftime('%d%m%Y')
time = datetime.now().strftime('%X')

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise['name'].title(),
            "duration" : exercise['duration_min'],
            "calories" : exercise['nf_calories'],
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs)

    print(sheet_response.text)
