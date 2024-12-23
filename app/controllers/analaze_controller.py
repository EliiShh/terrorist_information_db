from flask import Blueprint, request, jsonify, render_template

from app.services.analaze_service import get_most_active_groups_for_regions, get_yearly_attack_change, damage_percentage
from app.templates.maps import avg_damage_percentage_to_map, most_active_groups_to_map, yearly_attack_change_to_map

analysis_blueprint = Blueprint("analysis", __name__)



# @analysis_blueprint.route('/api/connected_count/<string:device_id>', methods=['GET'])
# def count_devices_connected(device_id):
#     try:
#         res = count_devices_connected_service(device_id)
#         return jsonify(res), 200
#     except Exception as e:
#         error = str(e)
#         print(error)
#         return jsonify({'error': error}), 501
#
# from flask import Flask, render_template
#
# app = Flask(__name__)
@analysis_blueprint.route('/average_percentage_of_casualties_by_region/', defaults={'limit': None})
@analysis_blueprint.route('/average_percentage_of_casualties_by_region/<int:limit>')
def route_get_damage_percentage(limit):
    select_result = damage_percentage(limit)
    avg_damage_percentage_to_map(select_result)
    return render_template('map.html')



@analysis_blueprint.route('/most_active_groups_for_regions')
def route_get_most_active_groups_for_regions():
    select_result = get_most_active_groups_for_regions()
    most_active_groups_to_map(select_result)
    return render_template('map.html')



@analysis_blueprint.route('/yearly_attack_change/', defaults={'limit': None})
@analysis_blueprint.route('/yearly_attack_change/<int:limit>')
def route_get_yearly_attack_change(limit):
    select_result = get_yearly_attack_change(limit)
    yearly_attack_change_to_map(select_result)
    return render_template('map.html')

