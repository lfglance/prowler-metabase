from os import environ as env
from dotenv import load_dotenv

load_dotenv()


DB_PASS = env.get('DB_PASS')
DB_HOST = env.get('DB_HOST')
DB_USER = env.get('DB_USER', 'prowler')
DB_NAME = env.get('DB_NAME', 'prowler')
DB_PORT = env.get('DB_PORT', 5432)
CSV_DIR = env.get('CSV_DIR')