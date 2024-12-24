from app.repo.psql_repo.event_repo import get_yearly_attack_change_by_region
from app.repo.psql_repo.grop_repo import get_most_active_groups_in_region
from app.repo.psql_repo.region_repo import get_loc_for_region, get_all_regions, get_damage_percentage


def get_most_active_groups_for_regions():
    regions = get_all_regions()
    all_groups_most_active_by_regions = []
    for reg in regions:
        loc = get_loc_for_region(reg)
        all_groups_most_active_by_regions.append({"region_txt":reg, "latitude": loc[0] , "longitude":loc[1], "groups": get_most_active_groups_in_region(reg)})
    return all_groups_most_active_by_regions


def get_yearly_attack_change(limit = None):
    regions = get_all_regions()
    all_yearly_by_regions = []
    for reg in regions:
        loc = get_loc_for_region(reg)
        all_yearly_by_regions.append({"region_txt":reg, "latitude": loc[0] , "longitude":loc[1], "yearly": get_yearly_attack_change_by_region(reg, limit)})
    return all_yearly_by_regions



def damage_percentage(limit = None):
    result = get_damage_percentage()
    results_list = []
    for row in result:
        loc = get_loc_for_region(row[0])
        results_list.append(
            {'region_txt': row[0], 'avg_damage_percentage_per_event': row[1], 'latitude': loc[0], 'longitude': loc[1]})
    sort_list = sorted(results_list, key=lambda x: abs(x["avg_damage_percentage_per_event"]), reverse=True)
    return sort_list if not limit else sort_list[:limit]
