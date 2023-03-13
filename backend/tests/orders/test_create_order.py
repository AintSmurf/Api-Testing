import pytest

from backend.src.dao.products_dao import ProductsDAO
from backend.src.helpers.orders_helper import OrdersHelpers
from backend.src.helpers.costumers_helper import CustomerHelper

@pytest.fixture(scope='module')
def random_product_setup():

    # helpers objects
    pd_helper = ProductsDAO()

    # get product from db
    rand_product = pd_helper.get_random_product_from_db(1)
    product_id = rand_product[0]['ID']

    return product_id

@pytest.mark.orders
@pytest.mark.tcido1
def test_create_paid_order_guest_user(random_product_setup):

     #get from the setup
     product_id = random_product_setup

     #helpers objects
     order_helper = OrdersHelpers()

     # create order and update it if you would like and make the call
     inf0 = {"line_items": [
        {
            "product_id": product_id,
            "quantity": 1
        },
    ]}
     order_json = order_helper.create_order(additional_args=inf0)

     #verify response
     expected_products = [{'product_id': product_id}]
     order_helper.verify_order_is_created(order_json, 0, expected_products)

@pytest.mark.orders
@pytest.mark.tcido2
def test_create_paid_order_new_customer(random_product_setup):
     #helpers objects
     order_helper = OrdersHelpers()
     cs_helper = CustomerHelper()

     # get product from db
     product_id = random_product_setup

     # create order and update it if you would like and make the call
     cs_info = cs_helper.create_customer()
     cs_id = cs_info['id']
     inf0 = {"line_items": [
        {
            "product_id": product_id,
            "quantity": 1
        },
    ],
     'customer_id':cs_id
     }
     order_json = order_helper.create_order(additional_args=inf0)

     #verify response
     expected_products = [{'product_id': product_id}]
     order_helper.verify_order_is_created(order_json, cs_id, expected_products)

