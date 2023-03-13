from front.seleniumExtended import SeleniumExtended
from front.pages.locators.CheckoutLocators import CheckoutLoocators

class CheckoutPage(CheckoutLoocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def wait_until_email_displayed(self, email):
        self.sl.wait_until_element_contains_text(self.EMAIL_ADDRESS_FIELD, email)

    def fill_the_form(self, firstname, lastname, address, city, postalcode, phone, email_address):
        self.sl.wait_and_input_text(self.FIRST_NAME_FIELD, firstname)
        self.sl.wait_and_input_text(self.LAST_NAME_FIELD, lastname)
        self.sl.wait_and_input_text(self.STREET_ADDRESS_FIELD, address)
        self.sl.wait_and_input_text(self.CITY_FIELD, city)
        self.sl.wait_and_input_text(self.ZIPCODE_FIELD, postalcode)
        self.sl.wait_and_input_text(self.PHONE_FIELD, phone)
        self.sl.wait_and_input_text(self.EMAIL_ADDRESS_FIELD, email_address)
    def click_on_the_place_order_btn(self):
        self.sl.wait_and_click(self.PLACE_ORDER_BUTTON)

    def getID(self):
        return self.sl.wait_and_get_element_Text(self.ORDER_ID)

    def verify_order_received(self):
        return self.sl.wait_and_get_element_Text(self.ORDER_RECEIVED)
