import os
from woocommerce import API
from backend.src.configs.hosts_config import WOO_API_HOSTS
from backend.src.utilities.credentialsUtility import CredentialsUtility
import logging as logger

class WooAPIUtility():

    def __init__(self):
        self.Credentials = CredentialsUtility()
        wc_creds = self.Credentials.get_wc_api_keys()

        self.env = os.environ.get("ENV", "test")
        self.base_url = WOO_API_HOSTS[self.env]
        self.wcapi = API(
            url=self.base_url,
            consumer_key=wc_creds['wc_key'],
            consumer_secret=wc_creds['wc_secret'],
            version="wc/v3"
        )
    def get(self, wc_endpoint, params=None, expected_status_code=200):
        rs_api = self.wcapi.get(wc_endpoint, params=params)

        self.rs_status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.endpoint = wc_endpoint
        self.assert_status_code()

        logger.debug(f"POST API WOOCOMMERCE RESPONSE: {self.rs_json}")

        return self.rs_json

    def post(self, wc_endpoint, params=None, expected_status_code=200):
        rs_api = self.wcapi.post(wc_endpoint, data=params)

        self.rs_status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.endpoint = wc_endpoint
        self.assert_status_code()

        logger.debug(f"GET API WOOCOMMERCE REPONSE: {self.rs_json}")

        return self.rs_json


    #vaildate the response code
    def assert_status_code(self):
        assert self.rs_status_code == self.expected_status_code,\
            f'Expected status code{self.expected_status_code} but actual status code is{self.rs_status_code}'\
            f"URL:{self.endpoint}, Response Json: {self.rs_json}"



