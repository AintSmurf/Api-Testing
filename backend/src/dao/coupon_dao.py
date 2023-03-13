from backend.src.utilities.dbUtility import DBUtility
import os

class CouponDAO():

    def __init__(self):
        self.db_helper = DBUtility()

    def get_all_coupons(self):
        sql = f"SELECT * FROM {os.environ.get('DB_NAME')}.wp_posts WHERE `post_type` = 'shop_coupon';"
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql
