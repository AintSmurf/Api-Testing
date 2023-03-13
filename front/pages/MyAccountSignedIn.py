from front.pages.locators.MyAccountSignedInLocator import MyAccountSignedInLocator
from front.seleniumExtended import SeleniumExtended
from front.helpers.config_helpers import get_base_url
import logging as Logger

class MyAccountSignedIn(MyAccountSignedInLocator):
    endpoint ='/my-account/'

    def __init__(self,driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def wait_until_logout_locator_clickable(self):
        self.sl.wait_until_element_is_clickble(self.LOGOUT_LOCATOR)
