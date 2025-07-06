import pytest
from selenium import webdriver

from lesson_27.np_page_objects.search_page_np import NovaPoshtaSearchObj
from lesson_27.np_page_objects.result_np_page import ResultPage


@pytest.fixture(scope="session")
def np_tracking():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield NovaPoshtaSearchObj(driver)
    driver.quit()
