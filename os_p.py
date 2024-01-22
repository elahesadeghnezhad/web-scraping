import requests
from bs4 import BeautifulSoup
import os
import csv

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

def download_image(image_url, image_title, category_directory):
    response = requests.get(image_url)
    with open(os.path.join(category_directory, f"{image_title}.svg"), "wb") as file:
        file.write(response.content)
    print(f"Downloaded image: {image_title}")

def write_metadata(title, url, directory, user_id):
    print(f"Writing metadata for: {title}")
    csv_file = os.path.join(directory, "metadata.csv")
    is_file_exist = os.path.isfile(csv_file)

    try:
        with open(csv_file, "a", newline="") as file:
            writer = csv.writer(file)

            # Write header if the file doesn't exist
            if not is_file_exist:
                writer.writerow(["Title", "URL", "user_id"])

            # Write metadata
            writer.writerow([title, url, user_id])
    except Exception as e:
        print(f"Error writing metadata to CSV: {e}")
