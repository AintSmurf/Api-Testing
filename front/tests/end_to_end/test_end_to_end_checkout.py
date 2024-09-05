import pytest

from front.pages.CartPage import CartPage
from front.pages.HomePage import HomePage
from front.pages.checkoutpage import CheckoutPage
from front.helpers.MyAcccountHelper import (
    gernerate_random_email,
    generate_random_username,
)
from backend.src.dao.customers_dao import CustomersDAO


@pytest.mark.usefixtures("init_driver")
class TestEndToEndGuestUser:

    @pytest.mark.selenium
    @pytest.mark.tcids4
    def test_end_to_end_checkout_guest_user(self):

        # set up the driver
        my_homepage = HomePage(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)
        cs = CustomersDAO()

        # go to home page
        my_homepage.go_to_my_homepage()
        # add 1 item to cart
        my_homepage.add_item_to_cart()

        # go to cart page
        my_homepage.click_on_cart_button()

        # go to cart and verify
        product_names = cart_page.get_all_products()
        assert (
            len(product_names) == 1
        ), f"Expected single item in cart but found {len(product_names)}"

        # apply free coupon
        cart_page.apply_discount()

        cart_page.click_coupon_btn()
        text = cart_page.verify_cuppon()
        assert text == "Coupon code applied successfully.", (
            f"Expected text is 'Coupon code applied successfully'"
            f"but we got instead{text}"
        )
        # click on checkout
        cart_page.click_on_checkout_button()

        # # fill the details form
        temp_email = gernerate_random_email()
        checkout_page.fill_the_form(
            generate_random_username(),
            "snow",
            "St. Robert",
            "Alabama",
            "10573",
            "041111111111",
            temp_email,
        )

        # click on place order and verify statically
        checkout_page.click_on_the_place_order_btn()
        import pdb

        pdb.set_trace()
        id = checkout_page.getID()
        message = "Thank you. Your order has been received."
        text = checkout_page.verify_order_received()
        # verify order has been submited
        assert text == message, (
            f"Expected text is {message}" f"but we got instead {text}"
        )

        id_db = cs.get_customer_id(id)[0]["ID"]

        # #verify order received in db
        assert int(id) == id_db, f"expected id is {id} " f"but we got instead {id_db}"
