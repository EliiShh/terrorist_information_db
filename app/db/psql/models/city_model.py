from app.db.psql.models import Base
from sqlalchemy import Column, Integer, String, Float, Date, Table, ForeignKey
from sqlalchemy.orm import relationship

class City(Base):
    __tablename__ = 'cities'

    city_id = Column(Integer, primary_key=True)
    city_name = Column(String)
    locations = relationship('Location', back_populates='city')