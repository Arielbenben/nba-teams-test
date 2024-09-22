from dataclasses import asdict
from functools import partial
from operator import attrgetter

import repository.fantasy_team_repository as f
from models.FantasyTeam import FantasyTeam
from repository.fantasy_team_repository import get_all_fantasy_teams_db
from repository.season_details_repository import get_season_details_by_player_id
from service.player_service import get_player_by_id_db
from toolz import pipe, partial


players_id = ['holidaa01', 'nesmiaa01', 'wiggiaa01', 'naderab01', 'murkead01']



def create_fantasy_team(ft: FantasyTeam):
    if not check_validate_positions(ft):
        return 'You chose players not in all positions, please try to fill all positions'
    return f.create_fantasy_team_to_db(ft)

def check_validate_positions(ft: FantasyTeam):
    positions = [ft.c_player_id, ft.pf_player_id, ft.sg_player_id, ft.sf_player_id, ft.pg_player_id]
    check = pipe(
        positions,
        partial(map, lambda x: get_season_details_by_player_id(x, 2024)),
        partial(map, lambda x: x.position),
        set,
        len
    )
    return check == 5

def delete_fantasy_team(team_name: str):
    return f.delete_fantasy_team_db(team_name)


def update_fantasy_name(ft: FantasyTeam):
    return f.update_fantasy_team_dc(ft)


def get_fantasy_team_by_id(team_id: int):
    return f.get_fantasy_teams_by_id_db(team_id)
# print(get_all_fantasy_teams_db())
# print(get_fantasy_team_by_id(3))
# print(create_fantasy_team(FantasyTeam(name='ariel', c_player_id="greenaj01", sf_player_id='lawsoaj01',
                                           # sg_player_id='griffaj01', pf_player_id='gordoaa01', pg_player_id='holidaa01')))