import requests
from bs4 import BeautifulSoup

proxies = {
    'http': 'http://127.0.0.1:2081',
    'https': 'http://127.0.0.1:2081',
}
api_key = "41944365-6514a9c6e238a11db6ad51ba1"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}

url = "https://pixabay.com/"
responds = requests.get(url=url,proxies=proxies)
print(responds.content)
soup = BeautifulSoup(response.text, "html.parser")
