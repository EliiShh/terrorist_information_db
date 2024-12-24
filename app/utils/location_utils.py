from geopy import Photon
import pandas as pd


def get_lat_lon(city, country_name):
    geolocator = Photon(user_agent="geoapi", timeout=10)
    try:
        location = geolocator.geocode(city)
        return {"type": "cities", "lat":location.latitude, "lon":location.longitude}
    except:
        location = geolocator.geocode(country_name)
        return {"type": "countries", "lat":location.latitude, "lon":location.longitude}




def fill_missing_lat_lon(df):
    cities = {}
    countries = {}
    missing_lat_lon = df[df['latitude'].isna() | df['longitude'].isna()]
    for row in missing_lat_lon.itertuples():
        city = row.city
        country = row.country_txt
        if city in cities:
            lat_lon = cities[city]
        elif pd.isna(city) and country in countries:
            lat_lon = countries[country]
        else:
            lat_lon = get_lat_lon(city, country)
            if lat_lon["type"] == "cities":
                cities[city] = lat_lon
            else:
                countries[country] = lat_lon
        df.at[row.Index, 'latitude'] = lat_lon['lat']
        df.at[row.Index, 'longitude'] = lat_lon['lon']
    return df