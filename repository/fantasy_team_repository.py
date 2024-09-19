from models.FantasyTeam import FantasyTeam
from repository.database import get_db_connection




def get_all_fantasy_teams_db():
   with get_db_connection() as connection:
       with connection.cursor() as cursor:
           cursor.execute("SELECT * FROM fantasy_team ")
           res = cursor.fetchall()
           all_fantasy_teams = [FantasyTeam(**p) for p in res]
           return all_fantasy_teams


def create_player_to_db(ft: FantasyTeam):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO fantasy_team (name, pg_player_id, sf_player_id, sg_player_id,
                           pf_player_id, c_player_id) 
                           VALUES (%s, %s, %s, %s, %s, %s) """,
                           (ft.name, ft.pg_player_id, ft.sf_player_id, ft.sg_player_id, ft.pf_player_id, ft.c_player_id))
            connection.commit()
            return

def update_fantasy_team_dc(ft: FantasyTeam):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE fantasy_team (pg_player_id, sf_player_id, sg_player_id,
                           pf_player_id, c_player_id) 
                           VALUES (%s, %s, %s, %s, %s) WHERE name = %s """,
                           (ft.pg_player_id, ft.sf_player_id, ft.sg_player_id, ft.pf_player_id, ft.c_player_id, ft.name))
            connection.commit()
            return

def delete_fantasy_team_db(ft_name):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""DELETE FROM  fantasy_team  WHERE name = %s """, (ft_name,))
            connection.commit()
            return


def get_fantasy_teams_by_id_db(team_id: int):
   with get_db_connection() as connection:
       with connection.cursor() as cursor:
           cursor.execute("SELECT * FROM fantasy_team WHERE id = %s ", (team_id,))
           res = cursor.fetchall()
           fantasy_team = FantasyTeam(id=res['id'], name=res['name'], pg_player_id=res['pg_player_id'],
                                           sf_player_id=res['sf_player_id'], sg_player_id=res['sg_player_id'],
                                           pf_player_id=res['pf_player_id'], c_player_id=res['c_player_id'])
           return fantasy_team