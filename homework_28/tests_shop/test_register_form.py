from faker import Faker
from homework_28.locators.user_profile_locators import ProfileLocators


class TestRegistration:

    def test_reg_func(self, web_driver, open_signup_window, fill_signup_form):
        fake = Faker()
        name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        password = fake.password()
        fill_signup_form(name, last_name, email, password)

        assert web_driver.find_element(*ProfileLocators.LOGOUT_BUTTON.value).is_displayed()
