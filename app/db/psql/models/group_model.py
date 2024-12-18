from app.db.psql.models import Base, event_group
from sqlalchemy import Column, Integer, String, Float, Date, Table, ForeignKey
from sqlalchemy.orm import relationship


class Group(Base):
    __tablename__ = 'groups'

    group_id = Column(Integer, primary_key=True)
    group_name = Column(String)
    events = relationship('Event', secondary=event_group, back_populates='groups')