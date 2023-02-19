##################### Normal Starting Project ######################

# 2. Check if today matches a birthday in the birthdays.csv

import datetime as dt
import pandas
import random
import smtplib

email = "forstudyadres@gmail.com"
password = "jmjgptlvxoomtrjv"
now = dt.datetime.now()
today_month = now.month
today_day = now.day

today = (today_month, today_day)


data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}



#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person['name'])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs=birthday_person['email'],
                            msg=f"Subcject:Happy Birthday! \n\n {contents}"
                            )





