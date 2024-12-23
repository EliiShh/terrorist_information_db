from . import Base
from sqlalchemy import Column, Integer, String, Float, Date, Table, ForeignKey
from sqlalchemy.orm import relationship

from .event_attacktype_model import event_attacktype
from .event_group_model import event_group
from .event_targettype_model import event_targettype


class Event(Base):
    __tablename__ = 'events'

    event_id = Column(Integer, primary_key=True)
    date = Column(Date)
    nkill = Column(Float)
    nwound = Column(Float)
    nperps = Column(Float)
    location_id = Column(Integer, ForeignKey('locations.location_id'))

    attacktypes = relationship('AttackType', secondary=event_attacktype, back_populates='events')
    targettypes = relationship('TargetType', secondary=event_targettype, back_populates='events')
    groups = relationship('Group', secondary=event_group, back_populates='events')
    location = relationship('Location', back_populates='events')