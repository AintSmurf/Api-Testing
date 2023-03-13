import os
import random
from backend.src.utilities.dbUtility import DBUtility

class CustomersDAO():

    def __init__(self):
        self.db_helper = DBUtility()

    def get_customer_by_email(self, email):
        sql = f"SELECT * FROM {os.environ.get('DB_NAME')}.wp_users where user_email = '{email}'; "
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql

    def get_random_customer_by_email(self, qty=1):
        if qty >= 5000:
            raise Exception(f"please Enter number less than 5000 you've entered:{qty}")


        sql = f"SELECT * FROM {os.environ.get('DB_NAME')}.wp_users ORDER BY id DESC LIMIT 5000;"
        rs_sql = self.db_helper.execute_select(sql)
        return random.sample(rs_sql, int(qty))

    def get_customer_id(self, ID):
        sql = f"SELECT * FROM {os.environ.get('DB_NAME')}.wp_posts where post_type = 'shop_order' and ID = {ID};"
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql


