import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
params = {"sol": 1000, "camera": "fhaz", "api_key": api_key}

response = requests.get(url, params=params)

photos = response.json().get("photos", [])

for i, photo in enumerate(photos[:5]):
    img_data = requests.get(photo["img_src"]).content
    with open(f"curiosity_photos/mars_photo{i + 1}.jpg", "wb") as f:
        f.write(img_data)
