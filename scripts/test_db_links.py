import json
import requests
from tqdm import tqdm
import sys
import argparse

def main(database):
    
    with open(database, 'rb') as fo:
        data = json.load(fo)

    batch = []
    errors = []
    
    for _, store in data.items():
        for test, vector in store.items():
            batch.append((test, vector))
    
    # NOTE: the script checks that the links are valid,
    # it doesn't check the integrity of the assets linked.
    for test, vector in tqdm(batch):
        try:
            mpdPath = vector["mpdPath"]
            assert test in mpdPath, f'unexpected path {mpdPath}'
            res = requests.head(mpdPath)
            assert res.status_code == 200, f'unexpected status {res.status_code} when checking {mpdPath}'

            zipPath = vector["zipPath"]
            assert test in zipPath, f'unexpected path {zipPath}'
            res = requests.head(zipPath)
            assert res.status_code == 200, f'unexpected status {res.status_code} when checking {zipPath}'
        
        except BaseException as e:
            errors.append(e)
            
    if len(errors) > 0:
        print(errors)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("database")
    args = parser.parse_args()
    main(args.database)
