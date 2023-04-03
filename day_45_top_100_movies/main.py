import requests
from bs4 import BeautifulSoup
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

tm_web = response.text

soup = BeautifulSoup(tm_web , "html.parser")
title_text= []


titles = soup.find_all(name="h3", class_="title")
# print(titles)
for title in titles:
    text = title.getText()
    title_text.append(text)

movies = title_text[::-1]
# print(movies)

with open ("movies.txt" , mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie} \n ")
