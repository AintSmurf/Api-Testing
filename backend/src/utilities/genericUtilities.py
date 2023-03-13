import logging as logger
import random
import string

def generate_random_email_and_password(domain=None, email_prefix=None):

    if not domain:
        domain ='test.com'
    if not email_prefix:
        email_prefix = 'testuser'
    random_email_string_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))
    email = email_prefix+'_' + random_string + '@' + domain

    password_length = 20
    random_password = ''.join(random.choices(string.ascii_letters, k=password_length))

    random_info = {'email': email, 'password': random_password}
    logger.debug(f'Randomly generated email and password:{random_info}')
    return random_info

def generate_random_string_for_product(length=10, prefix=None, suffix=None):
    random_string_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_string_length))
    if prefix:
        random_string += prefix
    if suffix:
        random_string += suffix

    return random_string
def generate_random_username(name=None):
    random_email_string_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))
    return random_string

def generate_random_coupon_name():
    random_cp_length = 10
    random_string = ''.join(random.choices(string.digits, k=random_cp_length))
    return  random_string


