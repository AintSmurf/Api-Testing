from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class SeleniumExtended:

    DEFAULT_TIMEOUT = 60

    def __init__(self, driver):
        self.driver = driver
    
    def _wait_for_condition(
        self, locator, condition, timeout=DEFAULT_TIMEOUT, text=None
    ):
        if text:
            return WebDriverWait(self.driver, timeout).until(condition(locator, text))
        return WebDriverWait(self.driver, timeout).until(condition(locator))

    def wait_and_input_text(self, locator, text, timeout=DEFAULT_TIMEOUT):
        self._wait_for_condition(
            locator, EC.visibility_of_element_located, timeout
        ).send_keys(text)

    def wait_until_element_contains_text(self, locator, text, timeout=DEFAULT_TIMEOUT):
        try:
            if not self._wait_for_condition(
                locator, EC.text_to_be_present_in_element, timeout, text
            ):
                raise Exception("couldnt find the locator")
        except TimeoutException:
            raise Exception("couldnt find the locator")

    def wait_until_element_is_clickble(self, locator, timeout=DEFAULT_TIMEOUT):
        self._wait_for_condition(locator, EC.element_to_be_clickable, timeout).click()

    def wait_and_get_elements(self, locator, timeout =None, err=None):
        err = (
            err
            if err
            else f"unable to find elements located by '{locator}'"
            f"after timeout of {timeout}"
        )
        try:
            el = self._wait_for_condition(
                locator, EC.visibility_of_all_elements_located, timeout
            )
        except TimeoutException:
            raise TimeoutException(err)
        return el

    def wait_and_get_element_Text(self, locator, timeout=DEFAULT_TIMEOUT):
        try:
            elm = self._wait_for_condition(
                locator, EC.visibility_of_element_located, timeout
            )
        except TimeoutException:
            raise TimeoutException()
        return elm.text







