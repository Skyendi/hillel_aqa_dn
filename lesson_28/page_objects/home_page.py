from lesson_28.page_objects.base_page import BasePage


class HomePage(BasePage):
    ENDPOINT = "https://www.automationexercise.com"

    def __init__(self, driver):
        super().__init__(driver)

