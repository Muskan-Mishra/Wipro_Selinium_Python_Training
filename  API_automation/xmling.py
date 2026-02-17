import requests
from lxml import html
url = "http://news.ycombinator.com"
response = requests.get(url)

data = html.fromstring(response.content)
title = data.find("./title").text
print(title)
#link
links = data.xpatht("//a/@herf")
print(links)

#link +url
links = data.xpatht("//a")
for link in links:
    print(link.text)
    print(link.get("herf"))

#extract the data using class name
titlelines = data.xpath("//span[@class = 'titleline]")
print(titlelines)
for title in titlelines:
    print(title.text)