from flasktasks import db
from flasktasks.database.seed import run_seed

if __name__ == '__main__':
    db.create_all()
    run_seed()
