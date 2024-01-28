import requests
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

def scrape(urlll, params):
    # send request to the pixabay
    response = requests.get(urlll, params=params)
    data = response.json()
    graphics = data["hits"]
    threads = []
    # extracting every image data 
    for graphic in graphics:
        graphic_name = graphic["tags"]
        graphic_link = graphic["pageURL"]
        graphic_userid = graphic["user_id"]
        graphic_directory = os.path.join("Graphics", graphic_name)
        os.makedirs(graphic_directory, exist_ok=True)
        # calling dowload_image function
        download_thread = Thread(target=download_image, args=(graphic_link, graphic_name, graphic_directory))
        threads.append(download_thread)
        download_thread.start()
        # calling write_metadata function
        metadata_thread = Thread(target=write_metadata, args=(graphic_name, graphic_link, graphic_directory, graphic_userid))
        threads.append(metadata_thread)
        metadata_thread.start()
    
    for thread in threads:
        thread.join()

def download_image(image_url, image_title, category_directory):
    response = requests.get(image_url)
    with open(os.path.join(category_directory, f"{image_title}.svg"), "wb") as file:
        file.write(response.content)

def write_metadata(title, url, directory, user_id):
    # creat a csv file
    csv_file = os.path.join(directory, "metadata.csv")
    is_file_exist = os.path.isfile(csv_file)
    # open the csv file
    with open("csv_file", "a", newline="") as file:
        writer = csv.writer(file)
        
        if not is_file_exist:
            writer.writerow(["Title"," Url", "Directory", "User_id"])
        
        writer.writerow([title, url, directory, user_id])
    
scrape(urlll,params)
print("finish")
