import requests
from bs4 import BeautifulSoup

proxies = {
    'http': 'http://127.0.0.1:2081',
    'https': 'http://127.0.0.1:2081',
}

url = "https://pixabay.com/vectors/"
responds = requests.get(url=url,proxies=proxies)
print(responds.content)
soup = BeautifulSoup(response.text, "html.parser")
categories = soup.find_all("a", class_="category")
for category in categories:
        category_name = category.text.strip()
        category_link = category["href"]
