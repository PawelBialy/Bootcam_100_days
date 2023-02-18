import  smtplib

# interia = "bootcamp.adres@interia.pl" # adres do nauki i wysyłania wiadomości - dla mojej informacji.
my_email = "bootcampadres1@gmail.com"
password = "hpauuromcgslqsqi"


with smtplib.SMTP("smtp.gmail.com", 587) as connection:  # tworzymy zmienną z smtplib i klasy SMTP. Dzięki temu łączymy się z pocztą.
    connection.starttls() # zabezpiecza naszą wiadomosc
    connection.login(user=my_email , password=password) # loguje do naszej poczty, musimy podac wartosci user i password.
    # podajemy od kogo wysyłamy wiadomość ( nasz email ) i adresata. Dodajemy też naszą wiadomość.
    connection.sendmail(
        from_addr=my_email,
        to_addrs="bootcamp.adres@interia.pl",
        msg="Subject: Hello \n\n This is the body of my email"
    ) # Subject: --> dodaje tytuł. \n\n pozwala na napiasnie wiadomosci :


