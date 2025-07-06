from enum import Enum

from selenium.webdriver.common.by import By

class SignupLoginLocators(Enum):
    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@data-qa='login-email']")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")
