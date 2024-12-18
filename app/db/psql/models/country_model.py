from app.db.psql.models import Base
from sqlalchemy import Column, Integer, String, Float, Date, Table, ForeignKey
from sqlalchemy.orm import relationship




class Country(Base):
    __tablename__ = 'countries'

    country_id = Column(Integer, primary_key=True)
    country_txt = Column(String)
    locations = relationship('Location', back_populates='country')