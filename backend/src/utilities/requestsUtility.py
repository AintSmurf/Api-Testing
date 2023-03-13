import json
import requests
import os
import logging as logger
from backend.src.configs.hosts_config import API_HOSTS
from requests_oauthlib import OAuth1
from backend.src.utilities.credentialsUtility import CredentialsUtility


class RequestsUtility():
    def __init__(self):
        self.Credentials = CredentialsUtility()
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1(self.Credentials.get_wc_api_keys().get('wc_key'),
                           self.Credentials.get_wc_api_keys().get('wc_secret'))

    # vaildate the response code
    def assert_status_code(self):
        assert self.rs_status_code == self.expected_status_code, \
            f'Expected status code{self.expected_status_code} but actual status code is{self.rs_status_code}' \
            f"URL:{self.url}, Response Json: {self.rs_json}"

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200) -> json:
        if not headers:
            headers = {"Content-Type": "application/json"}
        self.url = self.base_url + endpoint
        rs_api = requests.post(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.rs_status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"Api POST Response is:{rs_api.json()}")

        return rs_api.json()

    def get(self, endpoint, payload=None, headers=None, expected_status_code=200) -> json:
        if not headers:
            headers = {"Content-Type": "application/json"}
        self.url = self.base_url + endpoint
        rs_api = requests.get(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.rs_status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"Api GET Response is:{rs_api.json()}")

        return rs_api.json()

    def delete(self, endpoint, id_num=None, expected_status_code=200):
        self.url = self.base_url + endpoint + f'/{id_num}'
        rs_api = requests.delete(url=self.url, params={"force": True}, auth=self.auth)
        self.rs_status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()
        logger.debug(f"API DELETE Response is:{rs_api.json()}")
        return rs_api.json()

    def put(self, endpoint, id_num=None,payload=None, expected_status_code=200) -> json:
        self.url = self.base_url + endpoint + f'/{id_num}'
        rs_api = requests.put(url=self.url, params=payload, auth=self.auth)
        self.rs_status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()
        logger.debug(f"API PUT Response is:{rs_api.json()}")
        return rs_api.json()
