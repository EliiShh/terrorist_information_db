from . import Base
from sqlalchemy import Column, Integer, String, Float, Date, Table, ForeignKey
from sqlalchemy.orm import relationship

from .event_targettype_model import event_targettype


class TargetType(Base):
    __tablename__ = 'targettypes'

    targettype_id = Column(Integer, primary_key=True)
    targtype_txt = Column(String)
    events = relationship('Event', secondary=event_targettype, back_populates='targettypes')