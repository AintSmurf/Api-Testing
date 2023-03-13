from selenium.webdriver.common.by import By

class CheckoutLoocators():
    FIRST_NAME_FIELD =(By.ID, 'billing_first_name')
    LAST_NAME_FIELD = (By.ID, 'billing_last_name')
    STREET_ADDRESS_FIELD = (By.ID, 'billing_address_1')
    CITY_FIELD = (By.ID, 'billing_city')
    ZIPCODE_FIELD = (By.ID, 'billing_postcode')
    PHONE_FIELD = (By.ID, 'billing_phone')
    EMAIL_ADDRESS_FIELD = (By.ID, 'billing_email')
    PLACE_ORDER_BUTTON = (By.ID, 'place_order')
    ORDER_RECEIVED = (By.CSS_SELECTOR, 'p.woocommerce-thankyou-order-received')
    ORDER_ID = (By.CSS_SELECTOR, "li[class = 'woocommerce-order-overview__order order']>strong")
