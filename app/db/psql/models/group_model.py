from . import Base
from sqlalchemy import Column, Integer, String, Float, Date, Table, ForeignKey
from sqlalchemy.orm import relationship

from .event_group_model import event_group


class Group(Base):
    __tablename__ = 'groups'

    group_id = Column(Integer, primary_key=True)
    group_name = Column(String)
    events = relationship('Event', secondary=event_group, back_populates='groups')