import requests
from datetime import datetime
APP_ID = "5c54c69e"
API_KEY = "05964196295c83702d923317d6988d3c"
GENDER = "male"
WEIGHT = 93
HEIGHT = 190
AGE = 27

excercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/cd4cdf720a554ac4e1919d9c8297a553/myWorkouts/workouts"


exercise_text = input("Tell me which excercice you did: ")

headers = {
"x-app-id" : APP_ID,
"x-app-key" : API_KEY,
}


exercise_params = {
    "query" : exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT ,
    "age" : AGE,
}




response = requests.post(excercise_endpoint, json= exercise_params , headers=headers)
result = response.json()
# print(result)

today = datetime.now().strftime('%d%m%Y')
time = datetime.now().strftime('%X')

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise['user_input'].title(),
            "duration" : exercise['duration_min'],
            "calories" : exercise['nf_calories'],
        }
    }

    # sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs, )
    # print(sheet_inputs)
    #     print(sheet_response.text)

    #Basic auth
    # user = "pawelski"
    # password = "uczsieciulu"
    #
    # sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs, auth=(user, password))
    # print(sheet_response.text)

    #Token auth
    bearer_headers = {
        "Authorization": "Bearer cGF3ZWxza2k6dWN6c2llY2l1bHU",
    }

    sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=bearer_headers)
    print(sheet_response.text)
