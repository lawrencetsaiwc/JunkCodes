import requests
from bs4 import BeautifulSoup


url = "https://www.lexus.com.tw/"


response = requests.get(url, timeout=10)


objSoup = BeautifulSoup(response.text, "lxml")

print(objSoup.h4)