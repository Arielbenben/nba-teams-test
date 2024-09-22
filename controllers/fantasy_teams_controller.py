from flask import Blueprint, Flask, request, jsonify
import service.fantasy_team_service as f
from models.FantasyTeam import FantasyTeam

app = Flask(__name__)


fantasy_team_blueprint = Blueprint('teams', __name__)


@fantasy_team_blueprint.route('/<int:team_id>', methods=['GET'])
def get_fantasy_team_by_id(team_id):
    try:
        return jsonify({'fantasy team': f.get_fantasy_team_by_id(team_id)}), 200

    except Exception as e:
        return jsonify( { 'Error': str(e) } ), 500


@fantasy_team_blueprint.route('/<team_name>', methods=['DELETE'])
def delete_fantasy_team_by_name(team_name):
    try:
        f.delete_fantasy_team(team_name)
        return jsonify({ 'message': 'team deleted successfully' }), 200

    except Exception as e:
        return jsonify( { 'Error': str(e) } ), 500



@fantasy_team_blueprint.route('/<int:team_id>', methods=['PUT'])
def update_fantasy_team_by_name(team_id: int):
    try:
        json = request.json
        json['id'] = team_id
        f.update_fantasy_name(FantasyTeam(**json))
        return jsonify({ 'message': 'team updated successfully' }), 200

    except Exception as e:
        return jsonify( { 'Error': str(e) } ), 500



@fantasy_team_blueprint.route('/', methods=['POST'])
def create_fantasy_team():
    try:
        json = request.json

        if len(json) != 6:
            return jsonify({'message': 'You can not create team without 5 players, please enter 5 players.' })

        team = FantasyTeam(name=json['name'], pg_player_id=json['pg_player_id'],
                           sf_player_id=json['sf_player_id'], sg_player_id=json['sg_player_id'],
                           pf_player_id=json['pf_player_id'], c_player_id=json['c_player_id'])

        res = f.create_fantasy_team(team)
        if res:
            return jsonify({'message': res})
        return jsonify({ 'message': 'team created successfully' }), 200

    except Exception as e:
        return jsonify( { 'Error': str(e) } ), 500

# {
#     "name": "ariel",
#     "pg_player_id": "greenaj01",
#     "sf_player_id": "griffaj01",
#     "sg_player_id": "gordoaa01",
#     "pf_player_id": "holidaa01",
#     "c_player_id": "horfoal01"
# }