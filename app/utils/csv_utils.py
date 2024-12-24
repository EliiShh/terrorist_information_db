from datetime import datetime
import pandas as pd
import numpy as np
import ast


def read_csv_to_df(path:str, dtypes):
    try:
        df = pd.read_csv(path, encoding='latin1', dtype=dtypes, low_memory=False)
        return df
    except Exception as e:
        print(str(e))
        raise Exception


def convert_date(row):
    if row['imonth'] == 0:
        row['imonth'] = 1
    if row['iday'] == 0:
        row['iday'] = 1
    return datetime(row['iyear'], row['imonth'], row['iday'])



def convert_to_datetime(date_str):
    return datetime.strptime(date_str, '%d-%b-%y')


def normalize_date(date_str, y= datetime.now().year):
    date_obj = datetime.strptime(date_str, '%d-%b-%y')
    if date_obj.year > y:
        date_obj = date_obj.replace(year=date_obj.year - 100)
    return date_obj


def convert_groq_to_dict(stri):
    start_index = stri.find("{")
    end_index = stri.rfind("}")
    if start_index != -1 and end_index != -1:
        dict_str = stri[start_index:end_index + 1]
        try:
            n = ast.literal_eval(dict_str)
            r, t = n['region_txt'], n['targtype_txt']
            return {'region_txt': n.get('region_txt'), 'targtype_txt': n.get('targtype_txt')}
        except (ValueError, SyntaxError, KeyError, Exception):
            return {'region_txt': np.nan, 'targtype_txt': np.nan}
    return {'region_txt': np.nan, 'targtype_txt': np.nan}


