# import  smtplib
#
# # interia = "bootcamp.adres@interia.pl" # adres do nauki i wysyłania wiadomości - dla mojej informacji.
# my_email = "bootcampadres1@gmail.com"
# password = "hpauuromcgslqsqi"
#
#
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:  # tworzymy zmienną z smtplib i klasy SMTP. Dzięki temu łączymy się z pocztą.
#     connection.starttls() # zabezpiecza naszą wiadomosc
#     connection.login(user=my_email , password=password) # loguje do naszej poczty, musimy podac wartosci user i password.
#     # podajemy od kogo wysyłamy wiadomość ( nasz email ) i adresata. Dodajemy też naszą wiadomość.
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="bootcamp.adres@interia.pl",
#         msg="Subject: Hello \n\n This is a body of that email. "
#     ) # Subject: --> dodaje tytuł. \n\n pozwala na napiasnie wiadomosci :
#

# import datetime #  ten MODUŁ pozwala na wybaranie aktualnej dany i godziny
# datetime.datetime # "w" tym module wybieramy klase datatime czyli 1 datatime to moduł, 2 datatime to klasa z ktorej bierzemy
# # to jest to samo co w linikach 19-20 tylko w innym zapisie - bardziej czytelnym
# import datetime as dt
# now = dt.datetime.now()
# year = now.year # z tego atrybutu wypisujemy tylko to co potrzebujemy - tu rok
# if year == 2020:
#     print("hello")
# else:
#     print("It's not 2020")

# day_of_the_week = now.weekday()
# print(day_of_the_week)
# print(type (now))
#
# data_of_birth = dt.datetime(year= 1996, month=9,day=1, hour=6)   #wchodzimy do dt modułu i tworzymy nowy obiekt datatime,
# # musimy wypisac rok, miesiac, dzien - zapisujemy jak int.
# print(data_of_birth)

import smtplib
import datetime as dt
import random



my_email = "bootcampadres1@gmail.com"
password = "hpauuromcgslqsqi"
now = dt.datetime.now()
current_day = now.weekday()

if current_day == 6:
    with open("quotes.txt") as quotes_file :
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection :
        connection.starttls()
        connection.login(user=my_email, password=password, )
        connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:Motivation\n\n {quote}"
        )