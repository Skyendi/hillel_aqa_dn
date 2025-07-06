from enum import Enum

from selenium.webdriver.common.by import By


class BasePageLocators(Enum):
    SIGNUP_LOGIN_BUTTON  = (By.CSS_SELECTOR, "a[href='/login']")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[href='/logout']")
    BANNER_ACCEPT_BUTTON = (By.XPATH, "//button[@class='fc-button fc-cta-consent fc-primary-button']")