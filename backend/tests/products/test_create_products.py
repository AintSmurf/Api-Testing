import pytest

from backend.src.utilities.genericUtilities import generate_random_string_for_product
from backend.src.helpers.products_helper import ProductsHelper
from backend.src.dao.products_dao import ProductsDAO
import logging as logger

@pytest.mark.products
@pytest.mark.tcidp3
def test_create_single_product():
    #create demo payload
    payload = dict()
    payload['name'] = generate_random_string_for_product(10)
    payload['type'] = "simple"
    payload['regular_price'] = "10.99"

    #make the call
    pro_helper = ProductsHelper()
    pro_res = pro_helper.create_product(payload)
    pro_id = pro_res['id']
    logger.debug(f"creating product: response {pro_res} "
                 f"product id{pro_id}")

    #verify response not empty
    logger.info("verifying response is not empty")
    assert pro_res and pro_res['name'] == payload['name'],\
        "Failed to create Product response is empty"

    #verify its exists in db
    logger.info("verifying product is in the db !")
    pro_dao = ProductsDAO().get_product_with_id(pro_id)
    assert payload['name'] == pro_dao[0]['post_title'],\
    "Create product in db does not match the api title"\
    f"expected:{payload['name']}" \
    f"actual:{pro_dao[0]['post_title']}"








