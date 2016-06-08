from flasktasks import db

def run_seed():
    pass

if __name__ == '__main__':
    db.create_all()
    run_seed()
