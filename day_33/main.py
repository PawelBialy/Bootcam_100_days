import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json") # wywołujemy metode get z pakietu requests aby
# zdobyc dane które potrzebujemy z endpointu - endopoint to ten argument  nawiasie, wypisujemy go przy uzyciu url=" "

response.raise_for_status()

data = response.json()


longitude = data["iss_position"]["longitude"] # wchodzimy głębiej w dane i wypisujemy sobie dokładnie to co potrzebujemy
# tak jak w dict za pomocą keyworda
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)


#  errors :
# 1XX - hold on, to nie koniec
# 2XX -  Here you Go , kod zakonczony sukcesem
# 3XX - go away - brak dostępu
# 4XX  - you screwed up - cos schrzaniłeś
# 5XX - i screwed up - serwer cos schrzanił

# request modul

