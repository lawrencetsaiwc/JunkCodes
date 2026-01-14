import requests
from bs4 import BeautifulSoup


url = "https://www.lexus.com.tw/"


response = requests.get(url)


objSoup = BeautifulSoup(response.text, "lxml")

img_all = objSoup.find_all("h2", limit=4)

for img in img_all:
    print(img.text)