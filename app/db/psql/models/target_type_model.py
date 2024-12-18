from app.db.psql.models import Base, event_targettype
from sqlalchemy import Column, Integer, String, Float, Date, Table, ForeignKey
from sqlalchemy.orm import relationship



class TargetType(Base):
    __tablename__ = 'targettypes'

    targtype_id = Column(Integer, primary_key=True)
    targtype_txt = Column(String)
    events = relationship('Event', secondary=event_targettype, back_populates='targettypes')