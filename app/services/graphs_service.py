
import matplotlib.pyplot as plt
from io import BytesIO
from app.repo.psql_repo.analysis_queries_1 import deadliest_attack_types, get_top_5_damage_targets


def attack_types_graph_service():
    data = deadliest_attack_types()

    labels = [item['attacktype'] for item in data]
    values = [item['total_damage'] for item in data]

    plt.figure(figsize=(10, 6))
    plt.bar(labels, values)
    plt.title('Deadliest Attack Types')
    plt.xlabel('Attack Type')
    plt.ylabel('Total Damage')
    plt.xticks(rotation=45, ha='right')

    buf = BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf


