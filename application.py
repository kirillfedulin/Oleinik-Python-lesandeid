import requests
import lxml
from bs4 import BeautifulSoup
import fake_useragent

link = "https://zastavok.net/"

respons = requests.get(link).text

soup = BeautifulSoup(respons, "lxml")
block_photo = soup.find("div", class_="block_photo")
images = block_photo.find_all("div", class_= "short_full")
print(images)
for img in images:
    img_url = img.find("a").get("href")
    image_link = f"{link}{img_url}"

    respons = requests.get(image_link).text

    soup = BeautifulSoup(respons, "lxml")
    download_block = soup.find("div", class_="block_down")
    download_link = download_block.find("a").get("href=")
    result_link = f"{link}{download_link}"
    respons = requests.get(result_link).content
    print(respons)