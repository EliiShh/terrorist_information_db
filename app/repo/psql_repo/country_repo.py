from app.db.psql.database import session_maker
from app.db.psql.models import Country, Location


def get_all_countries():
    with session_maker() as session:
        query = session.query(
            Country.country_txt).all()
    return [r[0] for r in query]



def get_loc_for_country(country_name):
    with session_maker() as session:
        result = session.query(
            Location.latitude,
            Location.longitude
        ).join(Country, Location.country_id == Country.country_id) \
            .filter(Country.country_txt == country_name) \
            .first()
    return result

# region_name = "North America"
# print(get_loc_for_region(region_name))