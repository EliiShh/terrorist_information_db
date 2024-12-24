from sqlalchemy import func

from app.db.psql.database import session_maker
from app.db.psql.models import AttackType, Event, Region, Location, Group, Country, TargetType
from app.db.psql.models.event_group_model import event_group


def get_groups_type_by_country(country_name):
    with session_maker() as session:
        query = session.query(
            Group.group_name.label('group_name')
        ).join(Event.groups).join(Location, Event.location_id == Location.location_id) \
            .join(Country, Location.country_id == Country.country_id) \
            .filter(Country.country_txt == country_name).distinct(Group.group_name).all()

    return [g[0] for g in query]



# print(get_groups_type_by_country("Israel"))


def get_groups_type_by_region(region_name):
    with session_maker() as session:
        query = session.query(
            Group.group_name.label('group_name')
        ).join(Event.groups).join(Location, Event.location_id == Location.location_id) \
            .join(Region, Location.region_id == Region.region_id) \
            .filter(Region.region_txt == region_name).distinct(Group.group_name).all()

    return [g[0] for g in query]

# print(get_groups_type_by_region("Central America & Caribbean"))




def cooperation_between_groups():
    with session_maker() as session:
        query = session.query(Event).join(Event.groups).group_by(Event.event_id).having(func.count(Group.group_id) > 1).all()
        groups = []
        [groups.append([g.group_name for g in r.groups]) for r in query]
    return groups

# print(cooperation_between_groups())


#שאלה 8
def get_most_active_groups_in_region(region_name):
    with session_maker() as session:
            result = session.query(
            Group.group_name,
            func.count(Event.event_id).label('event_count')
        ).join(event_group, Group.group_id == event_group.c.group_id) \
         .join(Event, event_group.c.event_id == Event.event_id) \
         .join(Location, Event.location_id == Location.location_id) \
         .join(Region, Location.region_id == Region.region_id) \
         .filter(Region.region_txt == region_name) \
         .group_by(Group.group_name) \
         .order_by(func.count(Event.event_id).desc()) \
         .limit(5)

    return [{"Group":group.group_name, "Event Count": group.event_count} for group in result]

# print(get_most_active_groups_in_region("North America"))


