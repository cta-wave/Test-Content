import sys
from tcgen.database import Database
import requests
import csv
from tqdm import tqdm

batches = sorted([
    "2025-01-15",
    "2025-04-15",
    "2025-06-13",
    "2025-06-10"
])

profiles = [
    'chh1',
    'cud1',
    'clg1',
    'chd1'
]

def iter_db_entries(db):
    for p in profiles:
        for test_entry_key, db_entry in db.iter_entries(profile=p):
            yield test_entry_key, db_entry


def find_most_recent_batch(mpd_path):
    current_batch = mpd_path.split('/')[-2]
    most_recent_batch = current_batch
    for batch in batches:
        if batch > most_recent_batch:
            uri = mpd_batch_uri(mpd_path, batch)
            if requests.head(uri).status_code == 200:
                most_recent_batch = batch
    return current_batch, most_recent_batch

def mpd_batch_uri(mpd_path, batch):
    current = mpd_path.split('/')[-2]
    return str(mpd_path).replace(current, batch)

def main():
    database = sys.argv[1]
    db = Database()
    db.load(database)
    data = []

    db_entries = [(test_entry_key, db_entry["mpdPath"]) for test_entry_key, db_entry in iter_db_entries(db)]

    for test_entry_key, mpd_path in tqdm(db_entries):
        current_batch, most_recent_batch = find_most_recent_batch(mpd_path)
        if current_batch != most_recent_batch:
            data.append({
                'test_entry_key': test_entry_key,
                'current_batch': current_batch,
                'most_recent_batch': most_recent_batch
            })

    fieldnames = data[0].keys()
    with open('outdated.csv', 'w') as fo:
        writer = csv.DictWriter(fo, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
if __name__ == "__main__":
    main()