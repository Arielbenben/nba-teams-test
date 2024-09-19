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


def create_player_db(player: Player):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO players (playerName) VALUES (%s) ",
                           (player.playerName,))
            connection.commit()
            return

def get_player_by_id_db(player_id: int):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM players WHERE ID = %s", (player_id,))
            res = cursor.fetchall()
            player = Player(**res)
            connection.commit()
            return player

