import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "https://anaconda.org/channels/anaconda/packages/html5lib/overview"

    try:
        response = requests.get(url, timeout=10)  # 使用 requests.get(url) 來取得 url 的回應
        response.raise_for_status()                # 若 HTTP 狀態碼錯誤，拋出例外

        soup = BeautifulSoup(response.text, "lxml")  # lxml 是解析 html 文件方式

        print(soup.title.text)

    except requests.exceptions.Timeout:
        print("請求逾時")

    except requests.exceptions.ConnectionError:
        print("連線失敗")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP 錯誤: {e}")

    except Exception as e:
        print(f"其他錯誤: {e}")
