from sqlalchemy import text, func

from app.db.psql.database import session_maker
from app.db.psql.models import AttackType, Event, Region, Location, Group, Country, TargetType


# שאלה 13
def cooperation_between_groups():
    with session_maker() as session:
        q = session.query(Event).join(Event.groups).group_by(Event.event_id).having(func.count(Group.group_id) > 1).all()
        groups = []
        [groups.append([g.group_name for g in r.groups]) for r in q]
    return groups




#שאלה 15
def groups_that_attacked_targets_frequently():
    with session_maker() as session:
        sql_query = text("""
               SELECT
                    g.group_name,
                    tt.targtype_txt AS target_type,
                    COUNT(DISTINCT eg.event_id) AS attack_count
                FROM event_group eg
                JOIN groups g ON eg.group_id = g.group_id
                JOIN event_targettype et ON eg.event_id = et.event_id
                JOIN targettypes tt ON et.targettype_id = tt.targettype_id
                GROUP BY g.group_name, tt.targtype_txt
                HAVING COUNT(DISTINCT eg.event_id) > 2
                ORDER BY attack_count DESC;
           """)
        result = session.execute(sql_query)

    return [
        {'group_name': row[0], 'target_type': row[1], 'attack_count': row[2]}
        for row in result.fetchall()
    ]




