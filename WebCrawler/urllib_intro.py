import urllib.request
import requests

url = "https://www.toyotacpo.com.tw/"


response = urllib.request.urlopen(url)

print(response.read().decode("utf-8"))  # 使用 .decode("utf-8") 來解析中文內容