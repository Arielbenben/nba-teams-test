import psycopg2
from psycopg2.extras import RealDictCursor
from config.sql_config import SQL_URI



def get_db_connection():
    return psycopg2.connect(SQL_URI, cursor_factory=RealDictCursor)

def create_all_tables():
    create_table_players()
    create_table_season('2022')
    create_table_season('2023')
    create_table_season('2024')
    create_table_fantasy_team()
    return


def create_table_players():
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS players (
                id VARCHAR(100) PRIMARY KEY,
                name VARCHAR(100) NOT NULL
            )
            ''')
            connection.commit()
            return


def create_table_season(year: str):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS season_{year} (
                id SERIAL PRIMARY KEY,
                player_id VARCHAR(100) NOT NULL,
                team VARCHAR(100) NOT NULL,
                position VARCHAR(100) NOT NULL,
                games INTEGER,
                points INTEGER ,
                two_percent FLOAT,
                three_percent FLOAT,
                atr FLOAT,
                ppg_ratio FLOAT,
                FOREIGN KEY (player_id) REFERENCES players(id) ON DELETE CASCADE
            )
            ''')
            connection.commit()
            return


def create_table_fantasy_team():
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS fantasy_team (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                sg_player_id VARCHAR(100) NOT NULL,
                pf_player_id VARCHAR(100) NOT NULL,
                pg_player_id VARCHAR(100) NOT NULL,
                sf_player_id VARCHAR(100) NOT NULL,
                c_player_id VARCHAR(100) NOT NULL,
                FOREIGN KEY (sg_player_id) REFERENCES players(id) ON DELETE CASCADE,
                FOREIGN KEY (pf_player_id) REFERENCES players(id) ON DELETE CASCADE,
                FOREIGN KEY (pg_player_id) REFERENCES players(id) ON DELETE CASCADE,
                FOREIGN KEY (sf_player_id) REFERENCES players(id) ON DELETE CASCADE,
                FOREIGN KEY (c_player_id) REFERENCES players(id) ON DELETE CASCADE
            )
            ''')
            connection.commit()
            return

