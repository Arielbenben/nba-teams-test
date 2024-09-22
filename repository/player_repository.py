from models.Player import Player
from repository.database import get_db_connection


def get_all_players():
   with get_db_connection() as connection:
       with connection.cursor() as cursor:
           cursor.execute("SELECT * FROM players")
           res = cursor.fetchall()
           all_players = [Player(**p) for p in res]
           connection.commit()
           return all_players


def create_player_to_db(player: Player):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO players (id, name) VALUES (%s, %s) ",
                           (player.id, player.name,))
            connection.commit()
            return

def get_player_by_id_db(player_id: str):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM players WHERE ID = %s", (player_id,))
            res = cursor.fetchone()
            if not res:
                return None
            player = Player(id=res['id'], name=res['name'])
            return player

def get_player_name_by_player_id(player_id):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM players WHERE id = %s", (player_id,))
            player_name = cursor.fetchone()['name']
    return player_name

# print(get_all_players())