from app.db.psql.models import Base
from sqlalchemy import Column, Integer, String, Float, Date, Table, ForeignKey
from sqlalchemy.orm import relationship



class Location(Base):
    __tablename__ = 'locations'

    location_id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    region_id = Column(Integer, ForeignKey('regions.region_id'))
    city_id = Column(Integer, ForeignKey('cities.city_id'))
    country_id = Column(Integer, ForeignKey('countries.country_id'))

    region = relationship('Region', back_populates='locations')
    city = relationship('City', back_populates='locations')
    country = relationship('Country', back_populates='locations')
    event = relationship('Event', uselist=False, back_populates='location')