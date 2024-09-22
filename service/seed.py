from api.player_api import get_data_of_players_from_api
from repository.player_repository import get_all_players
from service.player_service import convert_player_from_api_to_model, create_player
from service.season_service import convert_season_details_from_api_to_model, create_season_details



def seed():
    if len(get_all_players()) > 0:
        return
    years = [2022, 2023, 2024]
    for year in years:
        data = get_data_of_players_from_api(year)
        for player in data:
            converted_player = convert_player_from_api_to_model(player)
            create_player(converted_player)
            converted_season = convert_season_details_from_api_to_model(player)
            create_season_details(converted_season, player['season'])
    return