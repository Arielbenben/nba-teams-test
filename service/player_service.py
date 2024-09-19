from functools import partial
from api.player_api import get_data_of_players_from_api
from models.Player import Player
from repository.player_repository import create_player_to_db
from toolz import pipe
from repository.player_repository import get_player_by_id_db
from service.season_service import get_data_season_from_api_and_save_db, create_season_details
from service.season_service import convert_season_details_from_api_to_model


def convert_player_from_api_to_model(player_data):
    return Player(name=player_data['playerName'], id=player_data['playerId'])

def create_player(player: Player):
    if check_if_already_exist(player.id):
        return
    return create_player_to_db(player)

def get_data_player_from_api_and_save_db():
    years = [2022, 2023, 2024]
    for year in years:
        data_json_api = get_data_of_players_from_api(year)
        for player in data_json_api:
            converted_player = convert_player_from_api_to_model(player)
            create_player(converted_player)
            converted_season = convert_season_details_from_api_to_model(player)
            create_season_details(converted_season, player['season'])
    return


def check_if_already_exist(player_id: str):
    check = get_player_by_id_db(player_id)
    return check

