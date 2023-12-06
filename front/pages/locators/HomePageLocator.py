from selenium.webdriver.common.by import By

class HomePageLocator():
    ADD_TO_CART_BUTTON =(By.XPATH, '//a[@data-product_sku="woo-beanie"]')
    CART_BUTTON =(By.XPATH, '//a[@href="http://localhost:8888/TestSite/cart/"]')
    VERIFCATION_TEXT =(By.CSS_SELECTOR, 'added_to_cart')

