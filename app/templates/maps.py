import folium
import os


def avg_damage_percentage_to_map(avgs:list):
    # חילוץ נקודת ההתחלה
    initial_location = [avgs[0]["latitude"], avgs[0]["longitude"]]
    map = folium.Map(location=initial_location)

    # הוספת כל הנקודות כמארקרים
    for i in avgs:
        cords = (i["latitude"], i["longitude"])
        folium.Marker(cords,
                      popup=f'region: {i["region_txt"]}, avg_damage_percentage_per_event:, '
                            f'{round(i["avg_damage_percentage_per_event"], 4)}').add_to(map)

    function_dir = os.path.dirname(__file__)
    map.save(f'{function_dir}\map.html')


def most_active_groups_to_map(most_active_groups:list):
    # חילוץ נקודת ההתחלה
    initial_location = [most_active_groups[0]["latitude"], most_active_groups[0]["longitude"]]
    map = folium.Map(location=initial_location)

    # הוספת כל הנקודות כמארקרים
    for i in most_active_groups:
        cords = (i["latitude"], i["longitude"])
        folium.Marker(cords,
                      popup=f'region: {i["region_txt"]}, groups_most_active:, '
                            f'{i["groups"]}').add_to(map)

    function_dir = os.path.dirname(__file__)
    map.save(f'{function_dir}\map.html')


def yearly_attack_change_to_map(most_active_groups:list):
    # חילוץ נקודת ההתחלה
    initial_location = [most_active_groups[0]["latitude"], most_active_groups[0]["longitude"]]
    map = folium.Map(location=initial_location)

    # הוספת כל הנקודות כמארקרים
    for i in most_active_groups:
        cords = (i["latitude"], i["longitude"])
        folium.Marker(cords,
                      popup=f'region: {i["region_txt"]}, yearly:, '
                            f'{i["yearly"]}').add_to(map)

    function_dir = os.path.dirname(__file__)
    map.save(f'{function_dir}\map.html')

