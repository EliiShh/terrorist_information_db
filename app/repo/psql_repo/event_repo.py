from sqlalchemy import func

from app.db.psql.database import session_maker
from app.db.psql.models import AttackType, Event, Region, Location, Group, Country, TargetType


def get_events_by_region(region_name):
    with session_maker() as session:
        query = session.query(
            TargetType.targtype_txt.label('target_type'),
            Group.group_name.label('group_name')
        ).join(Event.targettypes).join(Event.groups).join(Location, Event.location_id == Location.location_id)\
            .join(Region, Location.region_id == Region.region_id) \
            .filter(Region.region_txt == region_name).distinct(TargetType.targtype_txt, Group.group_name).all()

    return query


def get_events_by_country(country_name):
    with session_maker() as session:
        query = session.query(
            TargetType.targtype_txt.label('target_type'),
            Group.group_name.label('group_name')
        ).join(Event.targettypes).join(Event.groups).join(Location, Event.location_id == Location.location_id) \
            .join(Country, Location.country_id == Country.country_id)\
            .filter(Country.country_txt == country_name).distinct(TargetType.targtype_txt, Group.group_name).all()

    return query


#שאלה 6

def get_yearly_attack_change_by_region(region_name, limit=None):
    with session_maker() as session:
        result = session.query(
            func.extract('year', Event.date).label('year'),
            func.count(Event.event_id).label('event_count')
        ).join(Location, Event.location_id == Location.location_id) \
            .join(Region, Location.region_id == Region.region_id) \
            .filter(Region.region_txt == region_name) \
            .group_by(func.extract('year', Event.date)) \
            .order_by(func.extract('year', Event.date)) \
            .all()

    change_percentages = []
    for i in range(1, len(result)):
        previous_year_count = result[i - 1].event_count
        current_year_count = result[i].event_count
        if previous_year_count > 0:
            change_percentage = ((current_year_count - previous_year_count) / previous_year_count) * 100
        else:
            change_percentage = None
        change_percentages.append({
            "year": str(result[i].year),
            "change_percentage": change_percentage
        })
    change_percentages = [x for x in change_percentages if x["change_percentage"] is not None]
    sort_list = sorted(change_percentages, key=lambda x: abs(x["change_percentage"]), reverse=True)
    return sort_list if not limit else sort_list[:limit]