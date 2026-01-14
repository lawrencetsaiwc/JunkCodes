import requests
from bs4  import BeautifulSoup



url = "https://www.toyotacpo.com.tw/Home/Detail/57342"


response = requests.get(url)

objSoup = BeautifulSoup(response.text, "lxml")


li_txt_all = objSoup.select(".nav-item")

for li_txt in li_txt_all:
    print(li_txt.text)