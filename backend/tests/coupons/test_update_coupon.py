import pytest
from backend.src.helpers.coupon_helper import Coupon_Helper
from backend.src.dao.coupon_dao import CouponDAO

@pytest.mark.coupons
@pytest.mark.tcidco3

def test_update_coupon_percentage():

    # objects helpers
    cp_helper = Coupon_Helper()
    db_helper = CouponDAO()

    # get all the coupons from db
    db_response = db_helper.get_all_coupons()
    coupon_id = db_response[1]['ID']

    # #payload update
    payload = {"amount": "80"}


    # #verify in response
    rs_info = cp_helper.update_coupon_percentage(cp_id=coupon_id,payload=payload)

    #verify its updated in db
    assert db_response[1]['ID'] == rs_info['id'], f"supposed to update this coupon with ID:{db_response[1]['ID']}" \
                                                  f"but we updated different coupon wtih ID{rs_info['id']}"

    assert db_response[1]['post_title'] == rs_info['code'], f"name of the coupon supposed to be{rs_info['code']}" \
                                                            f"but we got different coupon {db_response[1]['post_title']}"
