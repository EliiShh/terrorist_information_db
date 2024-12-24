from app.db.psql.database import session_maker
from app.db.psql.models import AttackType, Event, Region, Location, Group
from sqlalchemy import text, func
import pandas as pd
from app.db.psql.models.event_group_model import event_group



#שאלה 1
def deadliest_attack_types(limit=5):
    with session_maker() as session:
        result = session.query(
            AttackType.attacktype_txt,
            func.sum(Event.nkill * 2 + Event.nwound).label('total_damage')
        ).join(Event.attacktypes).group_by(AttackType.attacktype_id).order_by(func.sum(Event.nkill * 2 + Event.nwound).desc()).limit(limit)
        return [{"attacktype": attacktype, "total_damage": total_damage} for attacktype, total_damage in result]


# print(deadliest_attack_types())

#שאלה 3
def get_top_5_damage_targets():
    with session_maker() as session:
        sql_query = text("""
            SELECT
                targettypes.targtype_txt,
                SUM(events.nkill * 2 + events.nwound) AS total_damage
            FROM events
            JOIN event_targettype ON events.event_id = event_targettype.event_id
            JOIN targettypes ON event_targettype.targettype_id = targettypes.targettype_id
            GROUP BY targettypes.targettype_id
            ORDER BY total_damage DESC LIMIT 5;
        """)
        result = session.execute(sql_query)
    return [{'targettype_txt': row[0], 'total_damage': row[1]} for row in result]

# print(get_top_5_damage_targets())






# # שאלה 2
# def get_damage_percentage():
#     with session_maker() as session:
#         sql_query = text("""
#             SELECT
#                 regions.region_txt,
#                 AVG((events.nkill * 2 + events.nwound) / NULLIF(events.event_id, 0)) AS avg_damage_percentage_per_event
#             FROM events
#             JOIN locations ON events.location_id = locations.location_id
#             JOIN regions ON locations.region_id = regions.region_id
#             GROUP BY regions.region_id
#             ORDER BY avg_damage_percentage_per_event DESC;
#         """)
#         result = session.execute(sql_query)
#     return result









# #שאלה 10
# def correlation_event(region: str):
#     session = session_maker()
#     result = session.query(
#         func.sum(Event.nkill * 2 + Event.nwound).label('total_damage'),
#         func.count(Event.event_id).label('event_count')
#     ).join(Location, Event.location_id == Location.location_id) \
#      .join(Region, Location.region_id == Region.region_id) \
#      .filter(Region.region_txt == region) \
#      .group_by(Region.region_txt).all()
#
#     session.close()
#
#     df = pd.DataFrame(result, columns=['total_damage', 'event_count'])
#     if len(df) > 1:
#         correlation = df['event_count'].corr(df['total_damage'])
#     else:
#         correlation = None
#     return correlation

# print(correlation_event("North America"))

# #שאלה 8
# def get_most_active_groups_in_region(region_name):
#     with session_maker() as session:
#             result = session.query(
#             Group.group_name,
#             func.count(Event.event_id).label('event_count')
#         ).join(event_group, Group.group_id == event_group.c.group_id) \
#          .join(Event, event_group.c.event_id == Event.event_id) \
#          .join(Location, Event.location_id == Location.location_id) \
#          .join(Region, Location.region_id == Region.region_id) \
#          .filter(Region.region_txt == region_name) \
#          .group_by(Group.group_name) \
#          .order_by(func.count(Event.event_id).desc()) \
#          .limit(5)
#
#     return [{"Group":group.group_name, "Event Count": group.event_count} for group in result]
#
# # print(get_most_active_groups_in_region("North America"))


# #שאלה 6
#
# def get_yearly_attack_change_by_region(region_name, limit=None):
#     with session_maker() as session:
#         result = session.query(
#             func.extract('year', Event.date).label('year'),
#             func.count(Event.event_id).label('event_count')
#         ).join(Location, Event.location_id == Location.location_id) \
#             .join(Region, Location.region_id == Region.region_id) \
#             .filter(Region.region_txt == region_name) \
#             .group_by(func.extract('year', Event.date)) \
#             .order_by(func.extract('year', Event.date)) \
#             .all()
#
#     change_percentages = []
#     for i in range(1, len(result)):
#         previous_year_count = result[i - 1].event_count
#         current_year_count = result[i].event_count
#         if previous_year_count > 0:
#             change_percentage = ((current_year_count - previous_year_count) / previous_year_count) * 100
#         else:
#             change_percentage = None
#         change_percentages.append({
#             "year": str(result[i].year),
#             "change_percentage": change_percentage
#         })
#     change_percentages = [x for x in change_percentages if x["change_percentage"] is not None]
#     sort_list = sorted(change_percentages, key=lambda x: abs(x["change_percentage"]), reverse=True)
#     return sort_list if not limit else sort_list[:limit]




# region_name = "North America"
# print(get_yearly_attack_change_by_region(region_name))


