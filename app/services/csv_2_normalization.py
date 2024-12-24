import datetime
import numpy as np
from app.utils.csv_utils import convert_date, read_csv_to_df, normalize_date, convert_groq_to_dict
import pandas as pd
from groq import Groq

from app.utils.location_utils import fill_missing_lat_lon


def groq_region_and_target(row):
    client = Groq(api_key="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",)
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": f"{row}.\"\n\n\nI need you to return me the region of the world it happened from among the following regions: ['Central America & Caribbean', 'North America', 'Southeast Asia', 'Western Europe', 'East Asia', 'South America', 'Eastern Europe', 'Sub-Saharan Africa', 'Middle East & North Africa', 'Australasia & Oceania', 'South Asia', 'Central Asia']\n and the type of people the attack was aimed at (such as Jews, gypsies, policemen, government officials, Christians) with the fields region_txt, targtype_txt\nDon't give me back anything but this dictionary"
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )
    response_content = ""
    for chunk in completion:
        response_content += chunk.choices[0].delta.content or ""
    return response_content

#
# response_content = groq_region_and_targt("24-Feb-68,Masada,Israel,Other,Explosives,0,0,\"ISRAEL.  Palestinian terrorists fired five mortar shells into the collective settlement at Masada, causing slight damage but no injuries.\"")
# result = convert_groq_to_dict(response_content)
# print(result)




def region_and_target_type(df):
    df["region_txt"] = np.nan
    df["targtype1_txt"] = np.nan
    df['region_txt'] = df['region_txt'].astype(str)
    df['targtype1_txt'] = df['targtype1_txt'].astype(str)

    for row in df.itertuples():
        response_content = groq_region_and_target(f"{row.Date} {row.City} {row.Country} {row.Weapon} {row.Description}")
        result = convert_groq_to_dict(response_content)
        df.at[row.Index, 'region_txt'] = result['region_txt']
        df.at[row.Index, 'targtype1_txt'] = result['targtype_txt']
        print(result)
    columns_to_check = ["region_txt", "targtype1_txt"]
    df[columns_to_check] = df[columns_to_check].replace("Unknown", np.nan)
    df[columns_to_check] = df[columns_to_check].replace("Other", np.nan)
    df[columns_to_check] = df[columns_to_check].replace("other", np.nan)
    df[columns_to_check] = df[columns_to_check].replace("None", np.nan)
    df[columns_to_check] = df[columns_to_check].replace('unknown/unspecified', np.nan)
    df[columns_to_check] = df[columns_to_check].replace('', np.nan)
    df[columns_to_check] = df[columns_to_check].replace(' ', np.nan)
    return df



def normalize_csv2(file_path):
    print("Normalizes the csv and completes the lat and lon")
    time_start = datetime.datetime.now()
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
    df['Date'] = df['Date'].apply(normalize_date)
    df.dropna(subset=["City", "Country", "Perpetrator"], how='all', inplace=True)
    columns_to_check = ["City", "Country", "Perpetrator", "Injuries", "Fatalities", "Weapon", "Description"]
    df = df.drop_duplicates(subset=columns_to_check, keep='first')

    df['City'] = df['City'].str.title()
    df['Country'] = df['Country'].str.title()
    df['Perpetrator'] = df['Perpetrator'].str.title()
    df['Weapon'] = df['Weapon'].str.title()
    df['Injuries'] = df['Injuries'].astype(int)
    df['Fatalities'] = df['Fatalities'].astype(int)
    df['Description'] = df['Description'].str.capitalize()

    pd.set_option('future.no_silent_downcasting', True)
    df[columns_to_check] = df[columns_to_check].replace("Unknown", np.nan)
    df[columns_to_check] = df[columns_to_check].replace("Other", np.nan)
    df = df.drop_duplicates(subset=columns_to_check, keep='first')
    # df = region_and_target_type(df.iloc[801:1201])
    df = region_and_target_type(df)
    df.rename(columns={"Country": "country_txt", 'City': 'city', 'Weapon': 'attacktype1_txt', 'Date': 'date', 'Perpetrator': 'gname',
                       'Fatalities': 'nkill', 'Injuries': 'nwound', 'Description': "summary"}, inplace=True)
    df["latitude"] = np.nan
    df["longitude"] = np.nan
    df = fill_missing_lat_lon(df)
    print(f"The normalization was successfully completed. time:{datetime.datetime.now() - time_start}")
    return df

