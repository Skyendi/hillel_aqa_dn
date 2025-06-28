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