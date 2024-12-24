from app.db.psql.database import session_maker
from app.db.psql.models import AttackType, Event
from sqlalchemy import text, func




#שאלה 1
def deadliest_attack_types(limit=5):
    with session_maker() as session:
        result = session.query(
            AttackType.attacktype_txt,
            func.sum(Event.nkill * 2 + Event.nwound).label('total_damage')
        ).join(Event.attacktypes).group_by(AttackType.attacktype_id).order_by(func.sum(Event.nkill * 2 + Event.nwound).desc()).limit(limit)
        return [{"attacktype": attacktype, "total_damage": total_damage} for attacktype, total_damage in result]



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






