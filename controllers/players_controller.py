from dataclasses import asdict
from typing import Optional
from flask import Flask, Blueprint, jsonify,request
from toolz import pipe, partial, first
from repository.season_details_repository import get_all_season_details
from repository.player_repository import get_player_name_by_player_id




app = Flask(__name__)


players_blueprint = Blueprint('players', __name__)


@players_blueprint.route('/', methods=['GET'])
def get_players_by_position():
    try:
        position = request.args.get('position', type=str)
        season = request.args.get('season', type=int)
        if season:
            return jsonify({'all players': get_all_players_per_position(season, position)}), 200

        return jsonify( { 'all players': {'2022': get_all_players_per_position(2022, position),
                         '2023': get_all_players_per_position(2023, position),
                         '2024': get_all_players_per_position(2023, position) }
                        }), 200

    except Exception as e:
        return jsonify( { 'Error': e } ), 500


def get_all_players_per_position(season: int, position: str):
    return pipe(
                get_all_season_details(season),
                partial(filter, lambda x: x.position == position),
                partial(map, asdict),
                list)
