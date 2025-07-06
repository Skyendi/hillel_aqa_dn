from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from lesson_28.locators.base_page import BasePageLocators
from selenium.webdriver.support import expected_conditions as ES



class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=10)
        self.actions = ActionChains(driver)
    @property
    def banner_accept_button(self):
        return self.wait.until(ES.element_to_be_clickable(BasePageLocators.BANNER_ACCEPT_BUTTON.value))

    @property
    def signup_login_button(self):
        return self.wait.until(ES.element_to_be_clickable(BasePageLocators.SIGNUP_LOGIN_BUTTON.value))

    @property
    def logout_page(self):
        return self.wait.until(ES.element_to_be_clickable(BasePageLocators.LOGOUT_BUTTON.value))

    def navigate_to_signup_login_page(self):
        from lesson_28.page_objects.signup_login_page import SignupLoginPage
        try:
           self.banner_accept_button.click()
        except TimeoutException:
            pass
        self.signup_login_button.click()
        return SignupLoginPage(self.driver)


