import requests
# from bs4 import BeautifulSoup
import csv
import os
from threading import Thread

urlll = "https://pixabay.com/api/"
num_images = 10
api_key = "41944678-39b6d49cec7fd580a769da914"
params = {
    "key": api_key,
    "image_type": "vector",
    "per_page": num_images
}
# scrape from pixabay
def scrape(urlll, params):
    response = requests.get(urlll, params=params)
    data = response.json()
    graphics = data["hits"]

    threads = []
    for graphic in graphics:
        graphic_name = graphic["tags"]
        graphic_link = graphic["pageURL"]
        graphic_userid = graphic["user_id"]

        # Create a directory for each graphic
        graphic_directory = os.path.join("Graphics", graphic_name)
        os.makedirs(graphic_directory, exist_ok=True)

        # Create a thread for downloading the vector graphic
        download_thread = Thread(target=download_image, args=(graphic_link, graphic_name, graphic_directory))
        threads.append(download_thread)
        download_thread.start()

        # Create a thread for writing metadata
        metadata_thread = Thread(target=write_metadata, args=(graphic_name, graphic_link, graphic_directory, graphic_userid))
        threads.append(metadata_thread)
        metadata_thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

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
        
scrape(urlll,params)
