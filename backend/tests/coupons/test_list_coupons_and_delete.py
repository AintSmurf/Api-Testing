import pytest
from backend.src.helpers.coupon_helper import Coupon_Helper
from backend.src.dao.coupon_dao import CouponDAO
import logging as logger


@pytest.mark.coupons
@pytest.mark.tcidco2
def test_delete_single_coupon_with_id():
    # objects helpers
    cp_helper = Coupon_Helper()
    db_helper = CouponDAO()

    #create payload for coupon  then call the post request
    payload = {"code": "50off",
               "discount_type": "percent",
               "amount": "50"}
    cp_helper.create_coupon(payload)

    #list all copouns and converts to dic as format of [id:code]
    rs_info = cp_helper.get_all_copouns()
    coupon_codes = {}
    for index in range(len(rs_info)):
        code = rs_info[index]['code']
        id = rs_info[index]['id']
        coupon_codes[code] = id

    #delete coupon with its id
    logger.info("the coupons you have in your'e store are:"
                f"{coupon_codes}")
    cp_id = coupon_codes['50off']
    rs_json = cp_helper.delete_specefic_coupon_with_id(cp_id)

    #verify coupon deleted from the response
    assert cp_id == rs_json['id'], f"expected id to delete:{cp_id}" \
                                   f"actual id from the response{rs_json['id']}"

    #verify coupon deleted with database
    db_response = db_helper.get_all_coupons()
    assert cp_id != db_response[-1]['ID'],f"The id not supposed to be in the db ID:{cp_id}" \
                                          f"but its not deleted ID:{db_response[-1]['ID']}"