import os
import pymysql
import logging as logger
from backend.src.utilities.credentialsUtility import CredentialsUtility


class DBUtility:

    _connection = None

    def __init__(self):
        creds_helper = CredentialsUtility()
        self.creds = creds_helper.get_db_credentials()
        if DBUtility._connection is None:
            DBUtility._connection = self.create_connection()

    def create_connection(self):
        logger.info(f"Initializing connection to SQLDataBase ...")
        if os.environ.get("PORT") == None:
            connection = pymysql.connect(
                host=os.getenv("DB_SERVER"),
                user=self.creds["db_user"],
                password=self.creds["db_password"],
                database=self.creds["db_name"],
            )
            return connection
        else:
            connection = pymysql.connect(
                host=os.getenv("DB_SERVER"),
                user=self.creds["db_user"],
                password=self.creds["db_password"],
                database=self.creds["db_name"],
                port=int(os.environ.get("PORT")),
            )
            return connection

    def execute_select(self, sql):
        connection = self.create_connection()
        DBUtility._connection =connection
        try:
            logger.info(f"Executing:{sql}")
            cur = DBUtility._connection.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Falied running sql: {sql} ERROR: {str(e)}")
        return rs_dict

    def seed_db(self, file_name):
        try:
            sql = self.get_the_sql_file(file_name)
            logger.info(f"Executing:{sql}")
            cur = DBUtility._connection.cursor(pymysql.cursors.DictCursor)
            sql_statements = sql.split(";")
            for statement in sql_statements:
                if statement.strip():
                    cur.execute(statement)
            DBUtility._connection.commit()
            cur.close()
        except Exception as e:
            raise Exception(f"Failed running SQL: {sql} ERROR: {str(e)}")

    def get_the_sql_file(self, file_name):
        script_directory = os.path.dirname(os.path.abspath(__file__))
        utlities_directory = os.path.dirname(script_directory)
        src_directory = os.path.dirname(utlities_directory)
        db_directory = os.path.join(src_directory, "sql")
        file = os.path.join(db_directory, file_name)
        with open(file, "r") as config_file:
            data = config_file.read()
        return data

    @classmethod
    def close_connection(cls):
        if cls._connection is not None:
            cls._connection.close()
            logger.info("Closed the SQLDataBase connection")
