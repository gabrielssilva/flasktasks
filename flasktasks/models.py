from flasktasks import db
from enum import Enum
from time import strftime


class Status(Enum):
    TO_DO = 1
    DOING = 2
    DONE = 3

class Color(Enum):
    GREY = 1
    BLUE = 2
    GREEN = 3
    YELLOW = 4
    RED = 5

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70))
    description = db.Column(db.String(140))
    status = db.Column(db.Integer)
    mission_id = db.Column(db.Integer, db.ForeignKey('mission.id'))

    def __init__(self, title, description, mission_id):
        self.title = title
        self.description = description
        self.status = Status.TO_DO.value
        self.mission_id = mission_id

class Mission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), unique=True)
    description = db.Column(db.String(210))
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    tasks = db.relationship('Task', backref='mission', lazy='dynamic')

    def __init__(self, title, description, tag_id):
        self.title = title
        self.description = description
        self.tag_id = tag_id

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    color = db.Column(db.Integer)
    missions = db.relationship('Mission', backref='tag', lazy='dynamic')

    def __init__(self, name, color=Color.GREY):
        self.name = name
        self.color = color.value
    
    def style(self):
        color = Color(self.color)
        return "tagged tag-%s" % color.name.lower()


class LogEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String(30))
    message = db.Column(db.String(140))

    def __init__(self, message):
        self.message = message
        self.timestamp = strftime("%d-%m-%Y %H:%M:%S")
