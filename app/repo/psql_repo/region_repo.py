from sqlalchemy import text

from app.db.psql.database import session_maker
from app.db.psql.models import Region, Location


def get_all_regions():
    with session_maker() as session:
        query = session.query(
            Region.region_txt).all()
    return [r[0] for r in query]




def get_loc_for_region(region_name):
    with session_maker() as session:
        result = session.query(
            Location.latitude,
            Location.longitude
        ).join(Region, Location.region_id == Region.region_id) \
            .filter(Region.region_txt == region_name) \
            .first()
    return result

# region_name = "North America"
# print(get_loc_for_region(region_name))


def get_damage_percentage():
    with session_maker() as session:
        sql_query = text("""
            SELECT
                regions.region_txt,
                AVG((events.nkill * 2 + events.nwound) / NULLIF(events.event_id, 0)) AS avg_damage_percentage_per_event
            FROM events
            JOIN locations ON events.location_id = locations.location_id
            JOIN regions ON locations.region_id = regions.region_id
            GROUP BY regions.region_id
            ORDER BY avg_damage_percentage_per_event DESC;
        """)
        result = session.execute(sql_query)
    return result