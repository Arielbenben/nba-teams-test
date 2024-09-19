from repository.database import create_all_tables
from service.player_service import get_data_player_from_api_and_save_db
from service.season_service import get_data_season_from_api_and_save_db
from service.seed import seed
from controllers.players_controller import players_blueprint
from flask import Flask
from controllers.fantasy_teams_controller import fantasy_team_blueprint



# app = Flask(__name__)
#
# if __name__ == "__main__":
# #
# #     create_all_tables()
# #     seed()

#     app.register_blueprint(players_blueprint, url_prefix="/api/players")
#       app.register_blueprint(fantasy_team_blueprint, url_prefix="/api/teams")
#     app.run(debug=True)