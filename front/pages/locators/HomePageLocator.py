from selenium.webdriver.common.by import By

class HomePageLocator():
    ADD_TO_CART_BUTTON =(By.CSS_SELECTOR, 'a.add_to_cart_button')
    CART_BUTTON =(By.XPATH, '//*[@id="modal-2-content"]/ul/li[1]/a')
    VERIFCATION_TEXT =(By.CSS_SELECTOR, 'added_to_cart')

