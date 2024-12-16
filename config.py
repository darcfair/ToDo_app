import os
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASS")
db_name = os.getenv("DB_NAME")
db_port = os.getenv("DB_PORT")
