from models.SeasonDetails import SeasonDetails
from repository.database import get_db_connection



def create_season_player_db(sd: SeasonDetails, year: int):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"""INSERT INTO season_{year} (player_id, team, position, games, points, two_percent, three_percent)
             VALUES (%s, %s, %s, %s, %s, %s, %s,) """,
                           (sd.player_id, sd.team, sd.position, sd.games, sd.points, sd.two_percent, sd.three_percent))
            connection.commit()
            return


def get_season_details_by_player_id(player_id: int, year: int):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT * FROM season_{year} WHERE player_id = %S """, (player_id,))
            res = cursor.fetchall()
            player_details = SeasonDetails(**res)
            return


def get_all_season_details(year: int):
   with get_db_connection() as connection:
       with connection.cursor() as cursor:
           cursor.execute(f"SELECT * FROM season_{year} ")
           res = cursor.fetchall()
           all_season_details = [SeasonDetails(**p) for p in res]
           connection.commit()
           return all_season_details