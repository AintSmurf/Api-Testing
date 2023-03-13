import os

from backend.src.utilities.dbUtility import DBUtility
import random


class ProductsDAO():

    def __init__(self):
        self.db_helper = DBUtility()

    def get_random_product_from_db(self, qty=1):

        if qty >= 5000:
            raise Exception(f"please Enter number less than 5000 you've entered:{qty}")


        sql = f"SELECT * FROM {os.environ.get('DB_NAME')}.wp_posts WHERE post_type = 'product' LIMIT 5000;"
        rs_sql = self.db_helper.execute_select(sql)
        return random.sample(rs_sql, int(qty))

    def get_product_with_id(self, id):
        sql = f"SELECT * FROM {os.environ.get('DB_NAME')}.wp_posts WHERE ID = {id}"
        return self.db_helper.execute_select(sql)

