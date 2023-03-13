import pytest
from backend.src.helpers.coupon_helper import Coupon_Helper
from backend.src.dao.coupon_dao import CouponDAO
from backend.src.utilities.genericUtilities import generate_random_coupon_name


@pytest.mark.coupons
@pytest.mark.tcidco1
def test_create_coupon():
    #objects helpers
    cp_helper = Coupon_Helper()
    db_helper = CouponDAO()

    #create payload for coupon then call the post request
    payload = {"code": generate_random_coupon_name(),
               "discount_type": "percent",
               "amount": "50"}
    rs_info = cp_helper.create_coupon(payload)

    #verify the coupon in response
    assert payload['code'] == rs_info['code'],"failed to create the coupon " \
                                                   f"expected ID{payload['code']}" \
                                                   f"actual ID{rs_info['code']}"
    #verify the coupon in db
    db_response = db_helper.get_all_coupons()
    assert db_response[-1]['ID'] == rs_info['id'], "failed to create the coupon " \
                                                   f"expected ID{rs_info['id']}" \
                                                   f"actual ID{db_response[-1]['ID']}"




