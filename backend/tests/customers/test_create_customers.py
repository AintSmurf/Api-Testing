import pytest

from backend.src.helpers.costumers_helper import CustomerHelper
from backend.src.utilities.genericUtilities import generate_random_email_and_password,generate_random_username
from backend.src.dao.customers_dao import CustomersDAO
from backend.src.utilities.requestsUtility import RequestsUtility

@pytest.mark.customers
@pytest.mark.tcidc1
def test_create_customer_only_email_password():
    rand_info = generate_random_email_and_password()
    email = rand_info.get('email')
    paswword = rand_info.get('password')
    username = generate_random_username()


    #create payload && make the call
    cust_object = CustomerHelper()
    cust_api_info = cust_object.create_customer(email=email, password=paswword, username=username)

    # verify email and user_name in the response
    assert cust_api_info['email'] == email,\
        f"Create Customer api return wrong email. expected Email:{email}, actual:{cust_api_info['email']}"
    assert cust_api_info['first_name'] == '',\
        f"Create Customer api returned value for first_name but its supposed return empty string"

    #verify customer is created in database
    cust_dao = CustomersDAO()
    cust_dao_info = cust_dao.get_customer_by_email(email)

    id_in_api = cust_api_info['id']
    id_in_db = cust_dao_info[0]['ID']
    assert id_in_api == id_in_db,\
        f"Creating the same customer failed" \
        f"actual id{id_in_db}" \
        f"expected id {id_in_api}"

@pytest.mark.customers
@pytest.mark.tcidc2
def test_create_customer_fail_for_existing_email():
    #get existing email from db
    cust_dau = CustomersDAO()
    cust_dau_info = cust_dau.get_random_customer_by_email()
    existing_email = cust_dau_info[0]['user_email']
    user_name = cust_dau_info[0]['display_name']

    #make call and create demo payload
    req_object = RequestsUtility()
    payload = {'email': existing_email, 'password': '123456', 'username':user_name}

    response = req_object.post(endpoint='customers', payload=payload, expected_status_code=400)
    assert response['code'] == 'registration-error-email-exists',\
        "Supposed to fail cause email Already exists"\
        "expected: 'registration-error-email-exists'" \
        f"actual:{response['code']}"

