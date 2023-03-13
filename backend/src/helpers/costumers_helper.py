from backend.src.utilities.genericUtilities import generate_random_email_and_password,generate_random_username
from backend.src.utilities.requestsUtility import RequestsUtility


class CustomerHelper():

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def create_customer(self, email=None, password=None, username=None, **kwargs):
        if not username:
            username = generate_random_username()
        if not email:
            ep = generate_random_email_and_password()
            email = ep.get('email')
        if not password:
            password = '123456'
        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload['username'] = username
        payload.update(kwargs)
        create_user_json = self.requests_utility.post('customers', payload=payload, expected_status_code=201)
        return create_user_json


