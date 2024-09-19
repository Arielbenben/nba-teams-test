from models.SeasonDetails import SeasonDetails
from repository.database import get_db_connection



def create_season_details_db(sd: SeasonDetails, year: int):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"""INSERT INTO season_{year} (player_id, team, position, games, points, two_percent, three_percent, 
            atr)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """,
                           (sd.player_id, sd.team, sd.position, sd.games, sd.points, sd.two_percent, sd.three_percent, sd.atr))
            connection.commit()
            return


def get_season_details_by_player_id(player_id: str, year: int):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT * FROM season_{year} WHERE player_id = %s """, (player_id,))
            res = cursor.fetchone()
            if not res:
                return
            player_details = SeasonDetails(player_id=res['player_id'], team=res['team'], position=res['position'], games=res['games'],
                                           points=res['points'], two_percent=res['two_percent'], three_percent=res['three_percent'],
                                           atr=res['atr'])
            return player_details


def get_all_season_details(year: int):
   with get_db_connection() as connection:
       with connection.cursor() as cursor:
           cursor.execute(f"SELECT * FROM season_{year} ")
           res = cursor.fetchall()
           if not res:
               return
           all_season_details = [SeasonDetails(player_id=p['player_id'], team=p['team'], position=p['position'],
                                               games=p['games'], points=p['points'], two_percent=p['two_percent'],
                                               three_percent=p['three_percent'], atr=p['atr']) for p in res]
           connection.commit()
           return all_season_details

