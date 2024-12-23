from . import Base
from sqlalchemy import Column, Integer, String, Float, Date, Table, ForeignKey
from sqlalchemy.orm import relationship
from .event_attacktype_model import event_attacktype


class AttackType(Base):
    __tablename__ = 'attacktypes'

    attacktype_id = Column(Integer, primary_key=True)
    attacktype_txt = Column(String)
    events = relationship('Event', secondary=event_attacktype, back_populates='attacktypes')