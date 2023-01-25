import psycopg2
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
HOST=os.getenv('HOST')
PORT=os.getenv('PORT')
DB=os.getenv('DB')
USER=os.getenv('USER')
PASSWORD=os.getenv('PASSWORD')

# HOST="localhost"
# PORT="5432"
# DB="emp"
# USER="postgres"
# PASSWORD="postgrespw"

psql_connection = psycopg2.connect(host=HOST, port=PORT, database=DB, user=USER, password=PASSWORD)
psql_connection.autocommit = True

def get_error_msg(type, response=None):
    if type.lower() == "get":
        return 200 if response is None else 500
    elif type.lower() == "post":
        return 200 if response is None else 500
    elif type.lower() == "delete":
        return 202 if response is None else 204

