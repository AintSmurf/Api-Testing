from backend.src.utilities.dbUtility import DBUtility

db_helper = DBUtility()
db_helper.seed_db("default.sql")