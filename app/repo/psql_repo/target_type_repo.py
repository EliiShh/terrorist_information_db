from app.db.psql.database import session_maker
from app.db.psql.models import AttackType, Event, Region, Location, Group, Country, TargetType


def get_grop_target_type_region(region_name):
    with session_maker() as session:
        query = session.query(
            TargetType.targtype_txt.label('target_type'),
            Group.group_name.label('group_name')
        ).join(Event.targettypes).join(Event.groups).join(Location, Event.location_id == Location.location_id)\
            .join(Region, Location.region_id == Region.region_id) \
            .filter(Region.region_txt == region_name).distinct(TargetType.targtype_txt, Group.group_name).all()

    return query


def get_grop_target_type_by_country(country_name):
    with session_maker() as session:
        query = session.query(
            TargetType.targtype_txt.label('target_type'),
            Group.group_name.label('group_name')
        ).join(Event.targettypes).join(Event.groups).join(Location, Event.location_id == Location.location_id) \
            .join(Country, Location.country_id == Country.country_id)\
            .filter(Country.country_txt == country_name).distinct(TargetType.targtype_txt, Group.group_name).all()

    return query