import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from app.repo.psql_repo.analysis_queries_1 import deadliest_attack_types, get_top_5_damage_targets
from app.repo.psql_repo.analysis_queries_2 import groups_that_attacked_targets_frequently
import seaborn as sns


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


def damage_targets_graph_service():
    data = get_top_5_damage_targets()

    labels = [item['targettype_txt'] for item in data]
    values = [item['total_damage'] for item in data]

    plt.figure(figsize=(10, 6))
    plt.bar(labels, values)
    plt.title('Top 5 Damage Targets')
    plt.xlabel('Target Type')
    plt.ylabel('Total Damage')
    plt.xticks(rotation=45, ha='right')

    buf = BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    buf.seek(0)

    return buf

def frequent_targets_graph():
    data = groups_that_attacked_targets_frequently()

    df = pd.DataFrame(data)
    pivot = df.pivot(index='group_name', columns='target_type', values='attack_count').fillna(0)

    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot, annot=True, fmt=".0f", cmap="coolwarm", cbar_kws={'label': 'Attack Count'})
    plt.title("Attack Counts by Group and Target Type")
    plt.xlabel("Target Type")
    plt.ylabel("Group Name")
    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf