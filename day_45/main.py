from bs4 import BeautifulSoup
import requests



response = requests.get("https://news.ycombinator.com")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []

for article in articles:
    text = article.getText()
    article_texts.append(text)
    link = article.find(name="a").get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
largest_number = max(article_upvotes)
# print(largest_number)
index_maxpt = article_upvotes.index(largest_number)
print(article_texts[index_maxpt])
print(article_links[index_maxpt])



# print(article_texts)
# print(article_links)
# print(article_upvotes)

























# article_tag = soup.find( class_="titleline" )
#
# print(article_tag.getText())


# with open ("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.prettify())
#
# class_is_heading = soup.find_all(name="a")
# print(class_is_heading)
