from selenium import webdriver
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from homework_28.locators.homepage_locators import HomePageLocators
from homework_28.locators.registration_form import RegistrationFormLocators
from homework_28.locators.user_profile_locators import ProfileLocators


@pytest.fixture(scope="session")
def web_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def open_signup_window(web_driver):
    wait = WebDriverWait(web_driver, timeout=10)
    signup_button = wait.until(EC.element_to_be_clickable(HomePageLocators.SIGN_UP_BUTTON.value))
    signup_button.click()

    yield web_driver


@pytest.fixture(scope="session")
def fill_signup_form(web_driver):
    def fill(name, lastname, email, password):
        wait = WebDriverWait(web_driver, timeout=10)
        wait.until(EC.element_to_be_clickable(RegistrationFormLocators.NAME_INPUT_FIELD.value)).send_keys(name)
        wait.until(EC.element_to_be_clickable(RegistrationFormLocators.LAST_NAME_INPUT_FIELD.value)).send_keys(lastname)
        wait.until(EC.element_to_be_clickable(RegistrationFormLocators.EMAIL_INPUT_FIELD.value)).send_keys(email)
        wait.until(EC.element_to_be_clickable(RegistrationFormLocators.PASSWORD_INPUT_FIELD.value)).send_keys(password)
        wait.until(EC.element_to_be_clickable(RegistrationFormLocators.RE_ENTER_PASSWORD_INPUT_FIELD.value)).send_keys(password)
        wait.until(EC.element_to_be_clickable(RegistrationFormLocators.REGISTER_BUTTON.value)).click()
        wait.until(EC.element_to_be_clickable(ProfileLocators.LOGOUT_BUTTON.value)).click()

    yield fill


