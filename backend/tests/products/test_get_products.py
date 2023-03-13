import pytest
from backend.src.utilities.requestsUtility import RequestsUtility
from  backend.src.dao.products_dao import ProductsDAO
import logging as logger

@pytest.mark.products
@pytest.mark.tcidp1
def test_list_all_products():
    #get all the products from the store
    logger.info("get all the products from the store")
    req_helper = RequestsUtility()
    rs_api = req_helper.get('products')
    assert rs_api,\
        "Get all products end point and returned nothing"

@pytest.mark.products
@pytest.mark.tcidp2
def test_list_product_with_specific_id():
    #get the id of the product
    logger.info("get the id of the product")
    pro_dao = ProductsDAO()
    pro_info = pro_dao.get_random_product_from_db()
    pro_id = pro_info[0]['ID']
    pro_name = pro_info[0]['post_title']

    #verify that the product exists in the store
    logger.info("verify that the product exists in the store")
    req_helper = RequestsUtility()
    rs_api = req_helper.get(f'products/{pro_id}')
    rs_api_name = rs_api['name']
    assert rs_api and pro_name == rs_api_name,\
        "Get product with specific id Falied" \
        f"expected id:{pro_id}" \
        f"actual id:{rs_api}"

