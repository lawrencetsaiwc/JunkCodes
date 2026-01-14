import requests
from bs4 import BeautifulSoup


url = "https://www.lexus.com.tw/"


response = requests.get(url)


objSoup = BeautifulSoup(response.text, "lxml")


print(objSoup.find_all("img", limit=4))