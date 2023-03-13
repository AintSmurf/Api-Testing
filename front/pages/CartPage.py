from front.seleniumExtended import SeleniumExtended
from front.helpers.config_helpers import get_base_url
from front.pages.locators.CartPageLocators import CartPageLocators


class CartPage(CartPageLocators):

    endpoint = "/cart/"

    def __init__(self,driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_cart_page(self):
        base_url = get_base_url()
        my_account_url = base_url + self.endpoint
        self.driver.get(my_account_url)

    def get_all_products(self):
        product_name_elements = self.sl.wait_and_get_elements(self.PRODUCT_NAMES_IN_CART)
        product_names = [p.text for p in product_name_elements]
        return product_names

    def click_on_checkout_button(self):
        self.sl.wait_and_click(self.CHECKOUT_BUTTON, 20)

    def apply_discount(self, cuopon_code):
        self.sl.wait_and_input_text(self.COUPON_TEXT_FIELD, cuopon_code)
    def verify_cuppon(self):
        text = self.sl.wait_and_get_element_Text(self.COUPON_MESSAGE)
        return text
    def click_coupon_btn(self):
        self.sl.wait_and_click(self.COUPON_BUTTON)

