from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flasktasks.db'
db = SQLAlchemy(app)

import flasktasks.views
import flasktasks.filters
import flasktasks.models
