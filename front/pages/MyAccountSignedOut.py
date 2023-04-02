from front.pages.locators.MyAccountSignedOutLocator import MyAccountSignedOutLocator
from front.seleniumExtended import SeleniumExtended
from front.helpers.config_helpers import get_base_url
import logging as logger

class MyAccountSignedOut(MyAccountSignedOutLocator):

    endpoint ='/my-account/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_my_account(self):
        base_url = get_base_url()
        my_account_url = base_url+self.endpoint
        logger.info(f"Going to: {my_account_url}")
        self.driver.get(my_account_url)

# Login functions
    def input_login_username(self, username):
        logger.info("Typing username in the field.")
        self.sl.wait_and_input_text(self.LOGIN_USER_NAME, username)

    def input_login_password(self, password):
        logger.info("Typing password in the field.")
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)

    def click_login_button(self):
        logger.info("clicking the Login button.")
        self.sl.wait_and_click(self.LOGIN_BUTTON)

    def wait_until_error_is_displayed(self, expected_error):
        logger.info("Showing the error displayed")
        self.sl.wait_until_element_contains_text(self.ERRORS_UL, expected_error)

# Register functions
    def input_register_username(self, username):
        logger.info("Typing username in the field.")
        self.sl.wait_and_input_text(self.REGISTER_USERNAME, username)

    def input_register_email(self, email):
        logger.info(f"Typing email:{email} in the field.")
        self.sl.wait_and_input_text(self.REGISTER_EMAIL, email)
    def input_register_password(self, password):
        logger.info("Typing password iin the field.")
        self.sl.wait_and_input_text(self.REGISTER_PASSWORD, password)


    def click_register_button(self):
        logger.info("clicking the register button.")
        self.sl.wait_and_click(self.REGISTER_BUTTON)

    def wait_until_register_error_pops_up(self, expected_error):
        self.sl.wait_and_get_element_Text(self.REGISTER_ERROR, expected_error)