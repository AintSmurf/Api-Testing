import os
import pymysql
import logging as logger
from backend.src.utilities.credentialsUtility import CredentialsUtility

class DBUtility():

    def __init__(self):
        creds_helper = CredentialsUtility()
        self.creds = creds_helper.get_db_credentials()

    def create_connection(self):
        if os.environ.get('PORT') == None:
            connection = pymysql.connect(host=os.getenv('DB_SERVER'),user=self.creds['db_user'],
                                         password=self.creds['db_password'], database=self.creds['db_name'])
            return connection
        else:
            connection = pymysql.connect(host=os.getenv('DB_SERVER'), user=self.creds['db_user'],
                                         password=self.creds['db_password'], database=self.creds['db_name'], port=int(os.environ.get("PORT")))
            return connection
    def execute_select(self,sql):
        conn = self.create_connection()
        try:
            logger.debug(f"Executing:{sql}")
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Falied running sql: {sql} ERROR: {str(e)}")
        finally:
            conn.close()

        return rs_dict



    def execute_sql(self,sql):
        pass
