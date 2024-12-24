import datetime
import os
from app.kafka_publisher.producer import send_data
from app.services.csv2_normlizaion import normalize_csv2
from app.services.csv_normalization_service import normalization_csv
from dotenv import load_dotenv

load_dotenv(verbose=True)

# def csv_1_to_kafka():
#     df = normalization_csv('../data/globalterrorismdb_0718dist.csv')
#     chunk_size = 500
#     time_start = datetime.datetime.now()
#     print("Enters the data into kafka")
#     for start in range(0, len(df), chunk_size):
#             chunk = df.iloc[start:start + chunk_size]
#             df_sliced = chunk[['date', 'latitude', 'longitude', 'summary']]
#             dict_obj = df_sliced.to_dict(orient='records')
#             topic_name = os.environ['TOPIC_EMAILS_NAME']
#             send_data(topic_name, dict_obj)
#             print(start)
#     print(f"kafka entry completed successfully. time:{datetime.datetime.now() - time_start}")


def csvs_to_kafka(df):
    chunk_size = 500
    time_start = datetime.datetime.now()
    print("Enters the data 2 into kafka")
    for start in range(0, len(df), chunk_size):
        chunk = df.iloc[start:start + chunk_size]
        df_sliced = chunk[['date', 'latitude', 'longitude', 'summary']]
        dict_obj = df_sliced.to_dict(orient='records')
        dict_obj["new"] = False
        topic_name = os.environ['TOPIC_EMAILS_NAME']
        send_data(topic_name, dict_obj)
        print(start)
    print(f"kafka entry completed successfully. time:{datetime.datetime.now() - time_start}")


if __name__ == "__main__":
    df = normalization_csv('../data/globalterrorismdb_0718dist.csv')
    csvs_to_kafka(df)


