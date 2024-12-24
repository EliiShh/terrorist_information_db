from app.repo.psql_repo.attack_type_repo import get_attack_type_by_region, get_attack_type_by_country
from app.repo.psql_repo.country_repo import get_loc_for_country, get_all_countries
from app.repo.psql_repo.grop_repo import get_groups_type_by_region, get_groups_type_by_country
from app.repo.psql_repo.region_repo import get_all_regions, get_loc_for_region
from app.repo.psql_repo.target_type_repo import get_grop_target_type_by_country, get_grop_target_type_region


def process_attack_type_results(results):
    attack_dict = {}
    for result in results:
        attacktype, group_name = result.attacktype, result.group_name
        if attacktype not in attack_dict:
            attack_dict[attacktype] = {
                'attacktype': attacktype,
                'groups': []
            }
        attack_dict[attacktype]['groups'].append(group_name)
    list_attack = list(attack_dict.values())
    for t in list_attack:
        if len(t["groups"]) < 2:
            list_attack.remove(t)
    return sorted(list_attack, key=lambda x: abs(len(x["groups"])), reverse=True)


def attack_type_by_country():
    countries_names = get_all_countries()
    res = []
    for c_name in countries_names:
         attack_types = process_attack_type_results(get_attack_type_by_country(c_name))
         if len(attack_types) == 0:
             continue
         loc = get_loc_for_country(c_name)
         res.append({"country_name":c_name, "latitude": loc[0] , "longitude":loc[1], "attack_type":attack_types[0]["attacktype"] , "groups": attack_types[0]["groups"]})
    return res


def attack_type_by_region():
    regions_names = get_all_regions()
    res = []
    for r_name in regions_names:
         attack_types = process_attack_type_results(get_attack_type_by_region(r_name))
         if len(attack_types) == 0:
             continue
         loc = get_loc_for_region(r_name)
         res.append({"region_name":r_name, "latitude": loc[0] , "longitude":loc[1], "attack_type":attack_types[0]["attacktype"] , "groups": attack_types[0]["groups"]})
    return res



def process_grop_target_type_results(results):
    target_dict = {}
    for result in results:
        target_type, group_name = result.target_type, result.group_name
        if target_type not in target_dict:
            target_dict[target_type] = {
                'target_name': target_type,
                'groups': []
            }
        target_dict[target_type]['groups'].append(group_name)
    list_targets = list(target_dict.values())
    for t in list_targets:
        if len(t["groups"]) < 2:
            list_targets.remove(t)
    return sorted(list_targets, key=lambda x: abs(len(x["groups"])), reverse=True)


def grop_target_type_by_country():
    countries_names = get_all_countries()
    res = []
    for c_name in countries_names:
         target_types = process_grop_target_type_results(get_grop_target_type_by_country(c_name))
         if len(target_types) == 0:
             continue
         loc = get_loc_for_country(c_name)
         res.append({"country_name":c_name, "latitude": loc[0] , "longitude":loc[1], "target_name":target_types[0]["target_name"] , "groups": target_types[0]["groups"]})
    return res

def grop_target_type_by_region():
    regions_names = get_all_regions()
    res = []
    for r_name in regions_names:
         target_types = process_grop_target_type_results(get_grop_target_type_region(r_name))
         if len(target_types) == 0:
             continue
         loc = get_loc_for_region(r_name)
         res.append({"region_name":r_name, "latitude": loc[0] , "longitude":loc[1], "target_name":target_types[0]["target_name"] , "groups": target_types[0]["groups"]})
    return res



def groups_type_by_country():
    countries_names = get_all_countries()
    res = []
    for c_name in countries_names:
         groups = get_groups_type_by_country(c_name)
         if len(groups) == 0:
             continue
         loc = get_loc_for_country(c_name)
         res.append({"country_name":c_name, "latitude": loc[0] , "longitude":loc[1], "count_groups":len(groups) , "groups": groups})
    return res




def groups_type_by_region():
    regions_names = get_all_regions()
    res = []
    for r_name in regions_names:
         groups = get_groups_type_by_region(r_name)
         if len(groups) == 0:
             continue
         loc = get_loc_for_region(r_name)
         res.append({"region_name":r_name, "latitude": loc[0] , "longitude":loc[1], "count_groups":len(groups) , "groups": groups})
    return res

