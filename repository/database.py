import psycopg2
from psycopg2.extras import RealDictCursor
from config.sql_config import SQL_URI



def get_db_connection():
    return psycopg2.connect(SQL_URI, cursor_factory=RealDictCursor)

def create_all_tables():
    return


def create_table_users():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS player (
        id SERIAL PRIMARY KEY,
        first VARCHAR(100) NOT NULL,
        last VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL
    )
    ''')
    connection.commit()
    cursor.close()
    connection.close()