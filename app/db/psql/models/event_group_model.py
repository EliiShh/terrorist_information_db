from app.db.psql.models import Base
from sqlalchemy import Column, Integer, String, Float, Date, Table, ForeignKey
from sqlalchemy.orm import relationship


event_group = Table(
    'event_group', Base.metadata,
    Column('event_id', Integer, ForeignKey('events.event_id')),
    Column('group_id', Integer, ForeignKey('groups.group_id'))
)