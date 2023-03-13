from backend.src.utilities.requestsUtility import RequestsUtility

class ProductsHelper():

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def create_product(self, payload):
        return self.requests_utility.post(endpoint='products', payload=payload,expected_status_code=201)
