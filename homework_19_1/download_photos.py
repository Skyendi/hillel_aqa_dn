import requests
import os
from dotenv import load_dotenv
from stream_logger import logger



def download_picture():

    api_key = os.getenv("API_KEY")
    url = os.getenv("base_url")
    params = {"sol": 1000, "camera": "fhaz", "api_key": api_key}

    response = requests.get(url, params=params)
    if response.status_code != 200:
        logger.error(f"Request ERROR, {response.status_code}")

    photos = response.json().get("photos", [])

    for i, photo in enumerate(photos[:5]):
        if "img_src" in photo:
            img_data = requests.get(photo["img_src"]).content
            with open(f"curiosity_photos/mars_photo{i + 1}.jpg", "wb") as f:
                f.write(img_data)
        else:
            logger.error(f"The key 'img_src' is not in 'photos'")
if __name__ == "__main__":
    load_dotenv()
    download_picture()