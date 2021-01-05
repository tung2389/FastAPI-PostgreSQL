import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
POSTGRE_SQL_DB = os.getenv("POSTGRE_SQL_DB")
POSTGRE_SQL_USER = os.getenv("POSTGRE_SQL_USER")
POSTGRE_SQL_PASSWORD = os.getenv("POSTGRE_SQL_PASSWORD")

db = psycopg2.connect(f'dbname={POSTGRE_SQL_DB} user={POSTGRE_SQL_USER} password={POSTGRE_SQL_PASSWORD}')