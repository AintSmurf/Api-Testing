from front.seleniumExtended import SeleniumExtended
from front.helpers.config_helpers import get_base_url
from front.pages.locators.CartPageLocators import CartPageLocators
from backend.src.utilities.credentialsUtility import CredentialsUtility


class CartPage(CartPageLocators):

    endpoint = "/cart/"

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)
        self.creds = CredentialsUtility()

    def go_to_cart_page(self):
        base_url = get_base_url()
        my_account_url = base_url + self.endpoint
        self.driver.get(my_account_url)

    def get_all_products(self):
        product_name_elements = self.sl.wait_and_get_elements(
            self.PRODUCT_NAMES_IN_CART
        )
        product_names = [p.text for p in product_name_elements]
        return product_names

    def click_on_checkout_button(self):
        self.sl.wait_until_element_is_clickble(self.CHECKOUT_BUTTON, 20)

    def apply_discount(self):
        coupon = self.creds.get_coupon()["COUPON"]
        self.sl.wait_and_input_text(self.COUPON_TEXT_FIELD, coupon, 30)

    def verify_cuppon(self):
        text = self.sl.wait_and_get_element_Text(self.COUPON_MESSAGE)
        self.sl.wait_until_element_contains_text(self.PRICE, "$0.00")
        return text

    def click_coupon_btn(self):
        self.sl.wait_until_element_is_clickble(self.COUPON_BUTTON)
