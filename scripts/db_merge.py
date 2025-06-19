import click
from tcgen.database import Database

@click.command()
@click.argument('database')
@click.argument('patch')
def merge(database, patch):
    db1 = Database()
    db1.load(database)
    
    db2 = Database()
    db2.load(patch)

    db1.merge(db2)
    db1.save(database)

if __name__ == '__main__':
    merge()