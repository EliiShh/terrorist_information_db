from app.db.psql.models import Base
from sqlalchemy import Column, Integer, String, Float, Date, Table, ForeignKey
from sqlalchemy.orm import relationship



class Region(Base):
    __tablename__ = 'regions'

    region_id = Column(Integer, primary_key=True)
    region_txt = Column(String)
    locations = relationship('Location', back_populates='region')