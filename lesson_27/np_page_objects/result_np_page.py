from selenium.webdriver.common.by import By
from lesson_27.np_page_objects.search_page_np import NovaPoshtaSearchObj
from lesson_27.locators.search_page_locators import SearchPageLocators
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC


class ResultPage(NovaPoshtaSearchObj):
    def __init__(self, web_driver):
        super().__init__(web_driver=web_driver)

    @property
    def ok_banner_button(self):
        return self.wait.until(EC.element_to_be_clickable(SearchPageLocators.OK_BANNER_BUTTON))

    @property
    def status(self):
        return self.wait.until(EC.visibility_of_element_located(SearchPageLocators.STATUS))

    def click_ok_button(self):
        self.ok_banner_button.click()

        return self
