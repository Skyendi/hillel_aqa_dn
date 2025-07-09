from lesson_28.conftest import web_driver_home_page
from lesson_28.page_objects.home_page import HomePage
from lesson_28.page_objects.signup_login_page import SignupLoginPage
import os
import time
from dotenv import load_dotenv
load_dotenv()

class TestLogin:

    def test_title_home_page(self, web_driver_home_page: HomePage):
        assert web_driver_home_page.driver.title == "Automation Exercise"

        # time.sleep(5)
        # breakpoint()

    def test_success_login(self, web_driver_home_page: HomePage):
        signup_login_page: SignupLoginPage = web_driver_home_page.navigate_to_signup_login_page()
        signup_login_page.make_login_with_creds(email=os.getenv("test_email"), password=os.getenv("test_password"))
        assert signup_login_page.logout_page.is_displayed()