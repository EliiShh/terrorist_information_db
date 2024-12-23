from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.settings.psql_config import psql_url
from app.db.psql.models import Base

engine = create_engine(psql_url)

session_maker = sessionmaker(bind=engine)


def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    init_db()

