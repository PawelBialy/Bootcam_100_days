import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWSAPI_KEY = "535c199b4a0b45b49424722a5a48b949"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
# API_KEY = "6B9UOT63T47NC7HF"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": "6B9UOT63T47NC7HF",
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key , value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data['4. close'])
print(yesterday_closing_price)

# - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data['4. close'])
print(day_before_yesterday_closing_price)
# - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

positive_diffrence = round(abs(yesterday_closing_price - day_before_yesterday_closing_price),3)
print(positive_diffrence)

# - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
# def percentage_diffrence(yesterday_closing_price, day_before_yesterday_closing_price):
diffrence = round((positive_diffrence / yesterday_closing_price) * 100)
print(diffrence)


# - If TODO4 percentage is greater than 5 then print("Get News").
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

news_parameters = {
    "apiKey": NEWSAPI_KEY,
    "qInTitle":  COMPANY_NAME,
}
if diffrence > 5:
    new_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    articles = new_response.json()["articles"]
    print(articles)

# Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
three_articles = articles[:3]
print(three_articles)

TWILIO_SID = "1248SDAS95as58ss"
TWILIO_AUTH_TOKEN = "48f2a535s2a932sadw"

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

# - Create a new list of the first 3 article's headline and description using list comprehension.
formatted_articles = [f"Headlines: {articles['title']}. \n Brief: {articles['description']} " for articles in three_articles ]

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

#TODO 9. - Send each article as a separate message via Twilio.
for articles in formatted_articles:
    for articles in formatted_articles:
        message = client.messages.create(
            body= articles,
            from_= "+154897625356",
            to= "my_number"
        )
#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

