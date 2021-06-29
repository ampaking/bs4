from bs4 import BeautifulSoup

import requests

response = requests.get("https://news.ycombinator.com/")
yc_comb_news = response.text

soup = BeautifulSoup(yc_comb_news, "html.parser")

artical_title = []
artical_url = []

story_title = soup.findAll(name="a", class_="storylink")
# print(story_title)
for i in story_title:
    title = i.text
    url = i["href"]
    artical_title.append(title)
    artical_url.append(url)

story_point = [int(story.text.split()[0]) for story in soup.findAll(name="span", class_="score")]
first_place = max(story_point)

my_index = story_point.index(first_place)
print(first_place)
print(artical_title[my_index])
print(artical_url[my_index])
print(story_point[my_index])


# with open("website.html") as html:
#     contents = html.read()
#
#
# soup = BeautifulSoup(contents, "html.parser")
#
# print(soup.title.string)
