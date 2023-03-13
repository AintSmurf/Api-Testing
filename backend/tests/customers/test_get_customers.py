import pytest
from backend.src.utilities.requestsUtility import RequestsUtility


@pytest.mark.customers
@pytest.mark.tcidc3
def test_get_all_customers():
    req_helper = RequestsUtility()
    rs_api = req_helper.get(endpoint='customers')

    assert rs_api,\
        f"Response of list all customers is Empty"

