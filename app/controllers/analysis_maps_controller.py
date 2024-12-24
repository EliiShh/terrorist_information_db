from flask import Blueprint, request, jsonify, render_template

from app.services.analysis_1_service import get_most_active_groups_for_regions, get_yearly_attack_change, damage_percentage
from app.services.analysis_2_service import attack_type_by_region, attack_type_by_country, grop_target_type_by_region, \
    grop_target_type_by_country, groups_type_by_region, groups_type_by_country
from app.templates.maps import avg_damage_percentage_to_map, most_active_groups_to_map, yearly_attack_change_to_map, \
    attack_type_by_region_to_map, attack_type_by_country_to_map, grop_target_type_by_region_to_map, \
    grop_target_type_by_country_to_map, groups_type_by_region_to_map, groups_type_by_country_to_map

analysis_blueprint = Blueprint("analysis", __name__)



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


@analysis_blueprint.route('/grop_target_type_by_loc/', defaults={'type_loc': "country"})
@analysis_blueprint.route('/grop_target_type_by_loc/<string:type_loc>')
def route_grop_target_type_by_by_location(type_loc):
    if type_loc == "region":
        select_result = grop_target_type_by_region()
        grop_target_type_by_region_to_map(select_result)
    else:
        select_result = grop_target_type_by_country()
        grop_target_type_by_country_to_map(select_result)
    return render_template('map.html')





@analysis_blueprint.route('/common_attack_type_by_location/', defaults={'type_loc': "country"})
@analysis_blueprint.route('/common_attack_type_by_location/<string:type_loc>')
def route_common_attack_type_by_location(type_loc):
    if type_loc == "region":
        select_result = attack_type_by_region()
        attack_type_by_region_to_map(select_result)
    else:
        select_result = attack_type_by_country()
        attack_type_by_country_to_map(select_result)
    return render_template('map.html')




@analysis_blueprint.route('/groups_type_by_location/', defaults={'type_loc': "country"})
@analysis_blueprint.route('/groups_type_by_location/<string:type_loc>')
def route_groups_type_by_location_by_location(type_loc):
    if type_loc == "region":
        select_result = groups_type_by_region()
        groups_type_by_region_to_map(select_result)
    else:
        select_result = groups_type_by_country()
        groups_type_by_country_to_map(select_result)
    return render_template('map.html')



