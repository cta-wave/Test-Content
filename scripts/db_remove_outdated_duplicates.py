import click
import json
from pathlib import Path

def deduplicate_table(table):
    clean = {}
    keys = {}
    for entry in table.keys():
        parts = entry.split("/")
        batch = parts[-2]
        parts = parts[:-2]
        k = "/".join(parts)
        if k in keys:
            keys[k].append(batch)
        else:
            keys[k] = [batch]
    for k, batches in keys.items():
        key = k + '/' + sorted(batches)[-1] + '/'
        clean[key] = table[key]
    return clean


@click.command()
@click.argument('database')
def deduplicate(database):
    clean = {}
    db_path = Path(database)
    with open(db_path, 'r') as dbfo:
        data = json.load(dbfo)
        for table_name, table in data.items():
            clean[table_name] = deduplicate_table(table)
    with open(db_path, 'w') as dbcfo:
        json.dump(clean, dbcfo, indent=4)

if __name__ == '__main__':
    deduplicate()