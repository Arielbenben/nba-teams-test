from repository.database import create_all_tables
from service.player_service import get_data_player_from_api_and_save_db
from service.season_service import get_data_season_from_api_and_save_db

# app = Flask(__name__)

if __name__ == "__main__":

    create_all_tables()
    get_data_player_from_api_and_save_db()
    # get_data_season_from_api_and_save_db()
#     app.register_blueprint(user_blueprint, url_prefix="/api/users")
#     app.register_blueprint(questions_blueprint, url_prefix="/api/questions")
#     app.run(debug=True)