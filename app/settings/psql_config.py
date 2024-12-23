import os
from dotenv import load_dotenv


load_dotenv(verbose=True)

psql_url = os.environ["PSQL_DB_URL"]


