from enum import Enum

from selenium.webdriver.common.by import By


class SearchPageLocators:
    SEARCH_INPUT = (By.XPATH, "//input[@class='track__form-group-input']")
    SEARCH_BUTTON = (By.ID, "np-number-input-desktop-btn-search-en")
    OK_BANNER_BUTTON = (By.XPATH,
                        "//button[@class='button v-btn v-btn--depressed v-btn--flat v-btn--outlined theme--light v-size--default']")
    STATUS = (By.XPATH, "//div[@class='header__status-text']")
