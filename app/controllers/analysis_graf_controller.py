from flask import Blueprint, jsonify
from flask import Response
from app.repo.psql_repo.analysis_queries_2 import groups_that_attacked_targets_frequently, cooperation_between_groups
from app.services.graphs_service import attack_types_graph_service, damage_targets_graph_service


analysis_graphs_blueprint = Blueprint("analysis_graphs", __name__)


@analysis_graphs_blueprint.route('/attack_types', methods=['GET'])
def attack_types_graph():
    try:
        buf = attack_types_graph_service()
        return Response(buf.getvalue(), mimetype='image/png')
    except Exception as e:
        return jsonify({'error': str(e)}), 501


@analysis_graphs_blueprint.route('/damage_targets', methods=['GET'])
def damage_targets_graph():
    try:
        buf = damage_targets_graph_service()
        return Response(buf.getvalue(), mimetype='image/png')
    except Exception as e:
        return jsonify({'error': str(e)}), 501

# 13
@analysis_graphs_blueprint.route('/cooperation_between_groups', methods=['GET'])
def cooperation_between_groups_route():
    try:
        res = cooperation_between_groups()
        return jsonify(res), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 501

# 15
@analysis_graphs_blueprint.route('/groups_frequent_targets', methods=['GET'])
def frequent_targets_graph():
    try:
        buf = groups_that_attacked_targets_frequently()
        return Response(buf.getvalue(), mimetype='image/png')
    except Exception as e:
        return jsonify({'error': str(e)}), 501