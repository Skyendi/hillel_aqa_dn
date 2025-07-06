from selenium import webdriver
import pytest
from lesson_28.page_objects.home_page import HomePage

@pytest.fixture(scope="session")
def web_driver_home_page():
    driver = webdriver.Chrome()
    driver.maximize_window()

    home_page = HomePage(driver=driver)
    home_page.driver.get(url=HomePage.ENDPOINT)

    yield home_page
    driver.quit()