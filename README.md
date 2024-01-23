# web-scraping
# Objective:
### The purpose of this Python Project Objective Develop a Python script or application to scrape vector graphics and their metadata from Pixabay, categorize them based on vector graphic categories, store them in an organized file system, and create a CSV file in each category folder containing detailed metadata of the vector graphics. This project will explore both serial and multithreaded programming approaches.
# How the project works:
### At first, we import the packages needed to run the code
### Then, we define the required variables for the request to the Pixabay site and the number of required images
### Next, we define the scrape function, which receives the image information from the API and creates a separate folder for each image, and creates threads for downloading the images and saving the metadata
### Then, the download_image function is defined, which downloads the images and stores them in the corresponding folders
### Then, the write_metadata function is defined, which saves the metadata information to the CSV file

