import os

from selenium import webdriver

import pytest


@pytest.fixture
def selenium_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:8000/dz.html")

    yield driver

    driver.quit()
