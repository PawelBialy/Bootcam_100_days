from bs4 import BeautifulSoup

with open ("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())

class_is_heading = soup.find_all(name="a")
print(class_is_heading)
