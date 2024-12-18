from app.db.psql.models import Base, event_attacktype
from sqlalchemy import Column, Integer, String, Float, Date, Table, ForeignKey
from sqlalchemy.orm import relationship



class AttackType(Base):
    __tablename__ = 'attacktypes'

    attacktype_id = Column(Integer, primary_key=True)
    attacktype_txt = Column(String)
    events = relationship('Event', secondary=event_attacktype, back_populates='attacktypes')