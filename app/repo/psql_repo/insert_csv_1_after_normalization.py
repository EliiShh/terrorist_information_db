from app.db.psql.database import session_maker
from app.db.psql.models.attack_type_model import AttackType
from app.db.psql.models.city_model import City
from app.db.psql.models.country_model import Country
from app.db.psql.models.event_model import Event
from app.db.psql.models.group_model import Group
from app.db.psql.models.location_model import Location
from app.db.psql.models.region_model import Region
from app.db.psql.models.target_type_model import TargetType
from app.services.csv_1_normalization import normalization_csv
import datetime


def get_or_create_city(city_name, session):
    city = session.query(City).filter(City.city_name == city_name).first()
    if not city:
        city = City(city_name=city_name)
        session.add(city)
        session.flush()
    return city

def get_or_create_country(country_name, session):
    country = session.query(Country).filter(Country.country_txt == country_name).first()
    if not country:
        country = Country(country_txt=country_name)
        session.add(country)
        session.flush()
    return country

def get_or_create_region(region_name, session):
    region = session.query(Region).filter(Region.region_txt == region_name).first()
    if not region:
        region = Region(region_txt=region_name)
        session.add(region)
        session.flush()
    return region

def get_or_create_attack_type(attack_type_name, session):
    attacktype = session.query(AttackType).filter(AttackType.attacktype_txt == attack_type_name).first()
    if not attacktype:
        attacktype = AttackType(attacktype_txt=attack_type_name)
        session.add(attacktype)
        session.flush()
    return attacktype

def get_or_create_target_type(target_type_name, session):
    targettype = session.query(TargetType).filter(TargetType.targtype_txt == target_type_name).first()
    if not targettype:
        targettype = TargetType(targtype_txt=target_type_name)
        session.add(targettype)
        session.flush()
    return targettype

def get_or_create_group(group_name, session):
    group = session.query(Group).filter(Group.group_name == group_name).first()
    if not group:
        group = Group(group_name=group_name)
        session.add(group)
        session.flush()
    return group



def get_location(row, session):
    return session.query(Location).filter(Location.latitude == row['latitude'],
                                          Location.longitude == row['longitude']).first()

def process_location(row, session):
    location = get_location(row, session)
    if not location:
        location = Location(latitude=row['latitude'], longitude=row['longitude'])
        if not isinstance(row['city'], float):
            city = get_or_create_city(row['city'], session)
            location.city_id = city.city_id
        if not isinstance(row['country_txt'], float):
            country = get_or_create_country(row['country_txt'], session)
            location.country_id = country.country_id
        if not isinstance(row['region_txt'], float):
            region = get_or_create_region(row['region_txt'], session)
            location.region_id = region.region_id
    session.add(location)
    session.flush()
    return location

def process_event(row, location, session):
    if row['nkill'] >= 0: nkill = row['nkill']
    else: nkill = None

    if row['nwound'] >= 0: nwound = row['nwound']
    else: nwound = None

    if row['nperps'] >= 0: nperps = row['nperps']
    else: nperps = None
    event = Event(
        date=row['date'],
        nkill=nkill,
        nwound=nwound,
        nperps=nperps,
        location_id=location.location_id
    )
    session.add(event)
    session.flush()
    return event

def process_attacktype(attacktype_txt, event, session):
    if not isinstance(attacktype_txt, float):
        attacktype = get_or_create_attack_type(attacktype_txt, session)
        event.attacktypes.append(attacktype)
    return event

def process_targettype(targtype1_txt, event, session):
    if not isinstance(targtype1_txt, float):
        targettype = get_or_create_target_type(targtype1_txt, session)
        event.targettypes.append(targettype)
    return event

def process_group(gname, event, session):
    if not isinstance(gname, float):
        group = get_or_create_group(gname, session)
        event.groups.append(group)
    return event

def process_chunk(chunk, session):
    for index, row in chunk.iterrows():
        location = process_location(row, session)
        event = process_event(row, location, session)

        process_attacktype(row['attacktype1_txt'], event, session)
        process_attacktype(row['attacktype2_txt'], event, session)
        process_attacktype(row['attacktype3_txt'], event, session)

        process_targettype(row['targtype1_txt'], event, session)
        process_targettype(row['targtype2_txt'], event, session)
        process_targettype(row['targtype3_txt'], event, session)

        process_group(row["gname"], event, session)
        process_group(row["gname2"], event, session)
        process_group(row["gname3"], event, session)

        session.commit()

def insert_csv_1():
    df = normalization_csv('../../data/globalterrorismdb_0718dist.csv')
    chunk_size = 500
    time_start = datetime.datetime.now()
    print("Enters the data into psql")
    for start in range(0, len(df), chunk_size):
        with session_maker() as session:
            chunk = df.iloc[start:start + chunk_size]
            process_chunk(chunk, session)
            print(start)
    print(f"Data entry completed successfully. time:{datetime.datetime.now() - time_start}")

if __name__ == "__main__":
    insert_csv_1()



