from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_27.locators.search_page_locators import SearchPageLocators


class NovaPoshtaSearchObj:
    def __init__(self, web_driver):
        self.web_driver = web_driver
        self.wait = WebDriverWait(self.web_driver, timeout=10)
        self.action = ActionChains(self.web_driver)

    @property
    def search_field(self):
        return self.wait.until(EC.element_to_be_clickable(SearchPageLocators.SEARCH_INPUT))

    @property
    def search_button(self):
        return self.wait.until(EC.element_to_be_clickable(SearchPageLocators.SEARCH_BUTTON))

    def open(self):
        self.web_driver.get("https://tracking.novaposhta.ua/#/uk")

        return self

    def input_search_ttn(self, ttn: str):
        self.search_field.send_keys(ttn)

        return self

    def click_search_button(self):
        from lesson_27.np_page_objects.result_np_page import ResultPage
        self.search_button.click()

        return ResultPage(self.web_driver)
