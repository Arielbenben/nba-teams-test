import repository.fantasy_team_repository as f
from models.FantasyTeam import FantasyTeam



players_id = ['holidaa01', 'nesmiaa01', 'wiggiaa01', 'naderab01', 'murkead01']



def create_fantasy_team(players_id):
    for player in players_id:
        f.create_player_to_db(player)
    return

def delete_fantasy_team(team_name):
    return f.delete_fantasy_team_db(team_name)


def update_fantasy_name(ft: FantasyTeam):
    return f.update_fantasy_team_dc(ft)

def get_fantasy_team_by_id(team_id: int):
    return f.get_fantasy_teams_by_id_db(team_id)