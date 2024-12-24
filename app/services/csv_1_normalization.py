import numpy as np
from geopy import Photon
from app.utils.csv_utils import convert_date, read_csv_to_df
import datetime


def get_lat_lon(city, country_name):
    geolocator = Photon(user_agent="geoapi", timeout=10)
    try:
        location = geolocator.geocode(city)
        return {"type": "cities", "lat":location.latitude, "lon":location.longitude}
    except:
        location = geolocator.geocode(country_name)
        return {"type": "countries", "lat":location.latitude, "lon":location.longitude}


def fill_missing_lat_lon(df):
    missing_lat_lon = df[df['latitude'].isna() | df['longitude'].isna()]
    cities = {}
    countries = {}
    for idx, row in missing_lat_lon.iterrows():
        city = row['city']
        country = row['country_txt']
        if cities.get(city):
            lat_lon = cities[city]
        elif city == np.nan and countries.get(country):
            lat_lon = countries[country]
        else:
            lat_lon = get_lat_lon(city, country)
            if lat_lon["type"] == "cities":
                cities[city] = lat_lon
            else:
                countries[country] = lat_lon
        df.at[idx, 'latitude'] = lat_lon['lat']
        df.at[idx, 'longitude'] = lat_lon['lon']
        print(lat_lon)
    return df


def normalization_csv(path):
    print("Normalizes the csv and completes the lat and lon")
    time_start = datetime.datetime.now()
    dtypes = {
        'eventid': np.int64,
        'iyear': np.int64,
        'imonth': np.int64,
        'iday': np.int64,
        'country': np.int64,
        'region': np.int64,
        'latitude': np.float64,
        'longitude': np.float64,
        'nkill': np.float64,
        'nwound': np.float64,
        'nperps': np.float64,
        'attacktype1': np.int64,
        'targtype1': np.int64,
        'targtype1_txt': str,
        'attacktype1_txt': str,
        'country_txt': str,
        'region_txt': str,
        'gname': str,
        'city': str,
        'summary': str
    }
    df = read_csv_to_df(path, dtypes)
    df['date'] = df.apply(convert_date, axis=1)
    df.dropna(subset=["country_txt", "region_txt", "city"], how='all', inplace=True)


    columns_to_check = [
        "date", "country_txt", "region_txt", "city", "latitude", "longitude", 'gname', 'gname2', 'gname3',
        "attacktype1_txt", "attacktype2_txt", "attacktype3_txt", "targtype1_txt", "targtype2_txt", "targtype3_txt"
    ]
    df = df.drop_duplicates(subset=columns_to_check, keep='first')

    columns_to_update_unknown = [
        "country_txt", "region_txt", "city", "attacktype1_txt", "attacktype2_txt", "attacktype3_txt",
        "targtype1_txt", "targtype2_txt", "targtype3_txt", "gname", "gname2", "gname3", 'summary'
    ]
    df[columns_to_update_unknown] = df[columns_to_update_unknown].replace("Unknown", np.nan)
    df[columns_to_update_unknown] = df[columns_to_update_unknown].replace("", np.nan)
    df[columns_to_update_unknown] = df[columns_to_update_unknown].replace(" ", np.nan)


    df = fill_missing_lat_lon(df)
    columns_to_update_smaller_than_0 = ['nperps', 'nkill', 'nwound']
    df[columns_to_update_smaller_than_0] = df[columns_to_update_smaller_than_0].where(
        df[columns_to_update_smaller_than_0] >= 0, np.nan)
    print(f"The normalization was successfully completed. time:{datetime.datetime.now() - time_start}")
    return df

# #
# df = normalization_csv("../data/globalterrorismdb_0718dist-1000 rows.csv")
# # # "iyear","country_txt","region_txt","city","latitude","longitude","attacktype1_txt","attacktype2_txt",'attacktype3_txt','targtype1_txt','targtype2_txt','targtype3_txt','gname','gname2','gname3','nperps','nkill','nwound'
# print(df["latitude"])