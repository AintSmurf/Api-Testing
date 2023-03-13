import os
import json

from backend.src.dao.orders_dao import OrdersDAO
from backend.src.utilities.wooApiUtility import WooAPIUtility
from backend.src.utilities.requestsUtility import RequestsUtility

class OrdersHelpers():

    def __init__(self):
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))
        self.woo_helper = WooAPIUtility()
        self.rs_helper = RequestsUtility()

    def create_order(self, additional_args=None):

        payload_template = os.path.join(self.cur_file_dir, '..', 'data', 'create_order_payload.json')
        with open(payload_template) as f:
            payload = json.load(f)

        if additional_args:
            assert isinstance(additional_args, dict), f"Parameter 'additional args' must be dictionary but found {type(additional_args)}"
            payload.update(additional_args)
        rs_api = self.rs_helper.post('orders', payload=payload, expected_status_code=201)

        return rs_api

    @staticmethod
    def verify_order_is_created(order_json, cs_id, exp_products):
        db_helper = OrdersDAO()

        # verify response
        assert order_json, "Create order response is empty"
        assert order_json['customer_id'] == cs_id, "Create order as user expected to have specific ID" \
                                                   f"expected id:{cs_id}" \
                                                   f"actual id:{order_json['customer_id']}"
        assert len(
            order_json['line_items']) == len(exp_products), f"Expected only {len(exp_products)} item in order but found {len(order_json['line_items'])}"

        # verify db
        order_id = order_json['id']
        line_info = db_helper.get_order_lines_by_order_id(order_id)
        assert line_info, f"Create order, line item not found in DB. Order id:{order_id}"

        line_items = [i for i in line_info if i['order_item_type'] == 'line_item']
        assert len(line_items) == 1, f"Expected 1 line item but found{len(line_items)}.Order id:{order_id}"

        #get list of product ids in the response
        api_product_ids = [i['product_id'] for i in order_json['line_items']]

        for product in exp_products:
            assert product['product_id'] in api_product_ids, f"Create order does not have at least 1 expected product in DB." \
                                                             f"product id is: {product['product_id']} order id is: {order_id}"
