#web scrapping ---> extract desired data from HTML web pages
#BeautifulSoup is also to do so !!
import requests
from bs4 import BeautifulSoup

url = "https://twitter.com/dna"
response = requests.get(url)
#print(response.text)
soup = BeautifulSoup(response.text,"html.parser")
print("Type of soup is :-",type(soup))
#print(soup)
#print(soup.prettify())
print("Title is :-",soup.title.text)
print("********************")
pTags = soup.find_all("p")
for tag in pTags:
    print(tag)
print("---------------------")
#divTags = soup.find_all("div")
#print(divTags)
divTags = soup.find_all("div",class_= "js-tweet-text-container")
for tag in divTags:
    print(tag)
    print(tag.text)
    print("======")