
from selenium.webdriver.common.by import By

class MyAccountSignedOutLocator:

    LOGIN_USER_NAME = (By.ID, 'username')
    LOGIN_PASSWORD =(By.NAME, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[value="Log in"]')
    ERRORS_UL = (By.CLASS_NAME, 'woocommerce-error')
    REGISTER_USERNAME = (By.ID, 'reg_username')
    REGISTER_EMAIL=(By.ID, 'reg_email')
    REGISTER_BUTTON =(By.NAME, 'register')
    REGISTER_ERROR = (By.XPATH, '//*[@id="wp--skip-link--target"]/div[3]/div/div[1]/ul')
    REGISTER_PASSWORD = (By.ID, 'reg_password')
