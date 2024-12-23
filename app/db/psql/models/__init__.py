from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .event_model import Event
from .city_model import City
from .group_model import Group
from .region_model import Region
from .location_model import Location
from .country_model import Country
from .attack_type_model import AttackType
from .target_type_model import TargetType

