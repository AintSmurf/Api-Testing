from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class SeleniumExtended:

    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 10

    def wait_and_input_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, self.default_timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        try:
            WebDriverWait(self.driver, self.default_timeout).until(
                EC.visibility_of_element_located(locator)
            ).click()
        except Exception as e:
            sleep(2)
            WebDriverWait(self.driver, self.default_timeout).until(
                EC.visibility_of_element_located(locator)
            ).click()

    def wait_until_element_contains_text(self, locator, text, timeout =None):
        timeout = timeout if timeout else self.default_timeout
        try:
            WebDriverWait(self.driver, self.default_timeout).until(
                EC.text_to_be_present_in_element(locator, text)
            )
        except TimeoutException:
            sleep(2)
            WebDriverWait(self.driver, self.default_timeout).until(
                EC.text_to_be_present_in_element(locator, text)
            )
    def wait_until_element_is_clickble(self, locator, timeout =None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, self.default_timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def wait_and_get_elements(self, locator, timeout =None, err=None):
        timeout = timeout if timeout else self.default_timeout
        err = err if err else f"unable to find elements located by '{locator}'" \
                              f"after timeout of {timeout}"
        try:
            el = WebDriverWait(self.driver, self.default_timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(err)
        return el

    def wait_and_get_element_Text(self, locator, timeout =None):
        timeout = timeout if timeout else self.default_timeout
        try:
            elm = WebDriverWait(self.driver, self.default_timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise TimeoutException()
        return elm.text







