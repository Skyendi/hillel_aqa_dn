import time
import os
from dotenv import load_dotenv

load_dotenv()

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from stream_logger import logger


class TestSeleniumFrames:

    def test_frame_1(self, selenium_driver):
        frame_1_password = os.getenv("frame_1_password")
        frame_2_password = os.getenv("frame_2_password")
        frame_1 = selenium_driver.find_element(By.CSS_SELECTOR, "#frame1")

        selenium_driver.switch_to.frame(frame_1)
        frame_input = selenium_driver.find_element(By.CSS_SELECTOR, "#input1")
        frame_input.send_keys(frame_1_password)
        time.sleep(3)
        check_button = selenium_driver.find_element(By.XPATH, '//button[@onclick="verifyInput(\'input1\')"]')
        check_button.click()
        alert = Alert(selenium_driver)
        logger.info(f"TEXT Alert: {alert.text}")

        assert alert.text == "Верифікація пройшла успішно!"
        time.sleep(1)
        alert.accept()

        time.sleep(1)

        selenium_driver.switch_to.default_content()

        frame_2 = selenium_driver.find_element(By.CSS_SELECTOR, "#frame2")

        selenium_driver.switch_to.frame(frame_2)
        frame_input_2 = selenium_driver.find_element(By.CSS_SELECTOR, "#input2")
        frame_input_2.send_keys(frame_2_password)
        time.sleep(3)
        check_button_2 = selenium_driver.find_element(By.XPATH, '//button[@onclick="verifyInput(\'input2\')"]')
        check_button_2.click()
        alert_2 = Alert(selenium_driver)
        logger.info(f"TEXT Alert: {alert_2.text}")

        assert alert_2.text == "Верифікація пройшла успішно!"
        time.sleep(1)
        alert_2.accept()

        time.sleep(1)
