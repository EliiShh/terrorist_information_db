from app.db.psql.models import Base, event_attacktype, event_targettype, event_group
from sqlalchemy import Column, Integer, String, Float, Date, Table, ForeignKey
from sqlalchemy.orm import relationship




class Event(Base):
    __tablename__ = 'events'

    event_id = Column(Integer, primary_key=True)
    date = Column(Date)
    nkill = Column(Integer)
    nwound = Column(Integer)
    nperps = Column(Integer)
    location_id = Column(Integer, ForeignKey('locations.location_id'))

    attacktypes = relationship('AttackType', secondary=event_attacktype, back_populates='events')
    targettypes = relationship('TargetType', secondary=event_targettype, back_populates='events')
    groups = relationship('Group', secondary=event_group, back_populates='events')
    location = relationship('Location', back_populates='event')