from flask import Blueprint, Flask, request, jsonify
import service.fantasy_team_service as f
from models.FantasyTeam import FantasyTeam

app = Flask(__name__)


fantasy_team_blueprint = Blueprint('teams', __name__)


@fantasy_team_blueprint.route('/<int: team_id>', methods=['GET'])
def get_fantasy_team_by_id():
    try:
        team_id = request.args.get('team_id', type=int)
        return jsonify({'fantasy team': f.get_fantasy_team_by_id(team_id)}), 200

    except Exception as e:
        return jsonify( { 'Error': e } ), 500


@fantasy_team_blueprint.route('/<str: team_name>', methods=['DELETE'])
def delete_fantasy_team_by_name():
    try:
        team_name = request.args.get('team_id', type=str)
        f.delete_fantasy_team(team_name)
        return jsonify({ 'message': 'team deleted successfully' }), 200

    except Exception as e:
        return jsonify( { 'Error': e } ), 500



@fantasy_team_blueprint.route('/<int: team_id>', methods=['PUT'])
def update_fantasy_team_by_name():
    try:
        team_id = request.args.get('team_id', type=int)
        team = f.get_fantasy_team_by_id(team_id)
        f.update_fantasy_name(team)
        return jsonify({ 'message': 'team updated successfully' }), 200

    except Exception as e:
        return jsonify( { 'Error': e } ), 500



@fantasy_team_blueprint.route('/', methods=['POST'])
def delete_fantasy_team_by_name():
    try:
        json = request.json
        team = FantasyTeam(id=json['id'], name=json['name'], pg_player_id=json['pg_player_id'],
                           sf_player_id=json['sf_player_id'], sg_player_id=json['sg_player_id'],
                           pf_player_id=json['pf_player_id'], c_player_id=json['c_player_id'])

        f.create_fantasy_team(team)

        return jsonify({ 'message': 'team created successfully' }), 200

    except Exception as e:
        return jsonify( { 'Error': e } ), 500