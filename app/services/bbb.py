# import numpy as np
# from app.utils.csv_utils import convert_date, read_csv_to_df
# import pandas as pd
# from opencage.geocoder import OpenCageGeocode
# import datetime
#
# from geopy.geocoders import Photon
#
# def get_lat_lon(country_name):
#     geolocator = Photon(user_agent="geoapiExercises")
#     location = geolocator.geocode(country_name)
#     if location:
#         return {"lat":location.latitude, "lon":location.longitude}
#     else:
#         return None
#
# print(datetime.datetime.now())
# print(get_lat_lon("Jerusalem"))
#
#
# def get_lat_lonn(city):
#     OCG = OpenCageGeocode('02c7536dccf241d3819f2fdcd0760b07')
#     results = OCG.geocode(f"u'{city}'")
#     return {"let":results[0]['geometry']['lat'],
#                         "lon":results[0]['geometry']['lng']}
#
# print(datetime.datetime.now())
# print(get_lat_lonn("Jerusalem"))
#
#
# def normalization_csv(path):
#     dtypes = {
#         'eventid': np.int64,
#         'iyear': np.int64,
#         'imonth': np.int64,
#         'iday': np.int64,
#         'country': np.int64,
#         'region': np.int64,
#         'latitude': np.float64,
#         'longitude': np.float64,
#         'nkill': np.float64,
#         'nwound': np.float64,
#         'nperps': np.float64,
#         'attacktype1': np.int64,
#         'targtype1': np.int64,
#         'targtype1_txt': str,
#         'attacktype1_txt': str,
#         'country_txt': str,
#         'region_txt': str,
#         'gname': str,
#         'city': str,
#     }
#     df = read_csv_to_df(path, dtypes)
#     df['date'] = df.apply(convert_date, axis=1)
#     df.dropna(subset=["country_txt", "region_txt", "city", "latitude", "longitude"], how='all', inplace=True)
#     columns_to_check = [
#         "date", "country_txt", "region_txt", "city", "latitude", "longitude", 'gname', 'gname2', 'gname3',
#         "attacktype1_txt", "attacktype2_txt", "attacktype3_txt", "targtype1_txt", "targtype2_txt", "targtype3_txt"
#     ]
#     df = df.drop_duplicates(subset=columns_to_check, keep='first')
#
#     columns_to_update_unknown = [
#         "country_txt", "region_txt", "city", "attacktype1_txt", "attacktype2_txt", "attacktype3_txt",
#         "targtype1_txt", "targtype2_txt", "targtype3_txt", "gname", "gname2", "gname3"
#     ]
#     df[columns_to_update_unknown] = df[columns_to_update_unknown].replace("Unknown", np.nan)
#
#     columns_to_update_smaller_than_0 = ['nperps', 'nkill', 'nwound']
#     df[columns_to_update_smaller_than_0] = df[columns_to_update_smaller_than_0].where(df[columns_to_update_smaller_than_0] >= 0, np.nan)
#     return df




# "iyear","country_txt","region_txt","city","latitude","longitude","attacktype1_txt","attacktype2_txt",'attacktype3_txt','targtype1_txt','targtype2_txt','targtype3_txt','gname','gname2','gname3','nperps','nkill','nwound'



# df = normalization_csv("../data/globalterrorismdb_0718dist.csv")
#
# columns_to_check = ["latitude", "city"]
#
# # מספר השורות שבהן כל העמודות הן NaN
# num_all_nan = df[columns_to_check].isna().all(axis=1).sum()
#
# print(f"Number of rows where all columns {columns_to_check} are NaN: {num_all_nan}")
