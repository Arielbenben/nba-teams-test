from models.SeasonDetails import SeasonDetails
from repository.season_details_repository import create_season_details_db, get_all_season_details
from api.player_api import get_data_of_players_from_api
from repository.season_details_repository import get_season_details_by_player_id

def convert_season_details_from_api_to_model(season_data_api):
    return SeasonDetails(player_id=season_data_api['playerId'], team=season_data_api['team'], position=season_data_api['position'],
                         games=season_data_api['games'], points=season_data_api['points'], two_percent=season_data_api['twoPercent'],
                         three_percent=season_data_api['threePercent'], atr=calculate_atr(season_data_api))

def calculate_atr(season_data_api):
    if season_data_api['turnovers'] == 0:
        return season_data_api['assists']
    return season_data_api['assists'] / season_data_api['turnovers']


def create_season_details(sd: SeasonDetails, year: int):
    if check_if_already_exist(sd.player_id, year):
        return
    return create_season_details_db(sd, year)

def get_data_season_from_api_and_save_db():
    years = [2024]
    for year in years:
        data_json_api = get_data_of_players_from_api(year)
        for season_details in data_json_api:
            converted_season_details = convert_season_details_from_api_to_model(season_details)
            create_season_details(converted_season_details, season_details['season'])
    return


def check_if_already_exist(player_id: str, year: int):
    check = get_season_details_by_player_id(player_id, year)
    return check

