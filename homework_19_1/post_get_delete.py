import os
import requests
from dotenv import load_dotenv
from homework_19_1.download_photos import download_picture
load_dotenv()



class ApiClient:
    def __init__(self):
        self.base_url = os.getenv("MY_SERVER_URL")
        self._session = requests.Session()

    def download_picture(self):
        download_picture()

    def _post(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        return self._session.post(url=url, timeout=10, **kwargs)

    def _get(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        return self._session.get(url=url, timeout=20, **kwargs)

    def _delete(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        return self._session.delete(url=url, timeout=10, **kwargs)


class PictureClient(ApiClient):
    def post_picture(self, picture_path):
        with open(picture_path, "rb") as file:
            files = {"image": file}
            return self._post("/upload", files=files)

    def get_picture(self, filename, **kwargs):
        return self._get(f"/image/{filename}", **kwargs)

    def delete_picture(self, filename, **kwargs):
        return self._delete(f"/delete/{filename}", **kwargs)


client = PictureClient()
resp_post = client.post_picture("curiosity_photos/mars_photo1.jpg")
print(resp_post.status_code, resp_post.text)

headers = {"Content-Type": "text"}
resp_get = client.get_picture("mars_photo1.jpg", headers=headers)
print(resp_get.status_code, resp_get.text)

resp_del = client.delete_picture("mars_photo1.jpg")
print(resp_del.status_code)
