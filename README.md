# FlaskTasks

A simple Kanban board made with Flask


## Dependencies

**Make sure to use a `python3` environment.**

Install the Following dependencies.

* Python 3

* Flask
```
pip install flask
```

* SQLAlchemy
```
pip install flask_sqlalchemy
```

* Blinker
```
pip install blinker
```

* SQLite


## Running

Before running, you must create the database. Run the `setup_db.py` script to create an initial database and some sample data.
```
python setup_db.py
```

The development server can be started by running the `runserver.py` scrip.
```
python runserver.py
```

And finally browse to http://localhost:5000

## Running Tests

There is no script to run all tests at once yet, since FlaskTasks still does not us nose or anything like it yet. To execute the tests, run each test file as a module.

```
python -m flasktasks.tests.tags_tests
python -m flasktasks.tests.missions_tests
```
