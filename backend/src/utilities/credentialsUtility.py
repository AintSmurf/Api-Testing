import os


class CredentialsUtility():

    def __init__(self):
        self.wc_key = ''
        self.wc_secret = ''
        self.db_user = ''
        self.db_password = ''


    def get_wc_api_keys(self):
        self.wc_key = os.environ.get('WC_KEY')
        self.wc_secret = os.environ.get('WC_SECRET')

        if not self.wc_key or not self.wc_secret:
            raise Exception(f"The APi Credentials 'WC_KEY' and 'wc_secret' must be in env variable "
                            f"wc_key is:{self.wc_key} "
                            f"wc_secret is:{self.wc_secret}")
        else:
            return{'wc_key': self.wc_key, 'wc_secret': self.wc_secret}

    def get_db_credentials(self):
        self.db_user = os.environ.get('DB_USER')
        self.db_password = os.environ.get('DB_PASSWORD')
        self.db_name = os.environ.get("DB_NAME")

        if not self.db_user or not self.db_password:
            raise Exception(f"The DB Credentials 'DB_USER' and 'DB_PASSWORD' must be in env variable "
                            f"db_user is:{self.db_user} "
                            f"db_password is:{self.db_password}")
        else:
            return{'db_user': self.db_user, 'db_password': self.db_password, 'db_name': self.db_name}