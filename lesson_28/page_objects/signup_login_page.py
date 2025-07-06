from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from lesson_28.locators.signup_login import SignupLoginLocators
from lesson_28.page_objects.base_page import BasePage


class SignupLoginPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver)

    @property
    def login_password_input(self) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(SignupLoginLocators.LOGIN_PASSWORD_INPUT.value))

    @property
    def login_button(self) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(SignupLoginLocators.LOGIN_BUTTON.value))

    @property
    def login_email_input(self) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(SignupLoginLocators.LOGIN_EMAIL_INPUT.value))

    def make_login_with_creds(self, email: str, password: str):
        self.login_email_input.send_keys(email)
        self.login_password_input.send_keys(password)
        self.login_button.click()

        return self