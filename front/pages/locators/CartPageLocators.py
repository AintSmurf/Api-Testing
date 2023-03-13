from selenium.webdriver.common.by import By


class CartPageLocators():
    PRODUCT_NAMES_IN_CART = (By.CSS_SELECTOR, 'tr.cart_item td.product-name')
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, 'a.checkout-button')
    COUPON_TEXT_FIELD =(By.ID, 'coupon_code')
    COUPON_MESSAGE = (By.CSS_SELECTOR,'div.woocommerce-message')
    COUPON_BUTTON = (By.NAME, 'apply_coupon')
