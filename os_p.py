import requests
from bs4 import BeautifulSoup
import os

base_url = "https://pixabay.com/api/"
num_images = 10
api_key = "41944678-39b6d49cec7fd580a769da914"
params = {
    "key": api_key,
    "image_type": "vector",
    "per_page": num_images
}

def scrape(base_url, params):
    response = requests.get(base_url, params=params)
    data = response.json()
    graphics = data["hits"]
    # Create a directory for each graphic
    graphic_directory = os.path.join("VectorGraphics", graphic_name)
    os.makedirs(graphic_directory, exist_ok=True)
