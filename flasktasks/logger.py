from flasktasks import app, db
from flasktasks.models import LogEntry
from flasktasks.signals import task_created, mission_created 


@task_created.connect
def log_task_creation(task, **kwargs):
    message = "The task \"%s\" was created." % task.title
    log_entry(message)


@mission_created.connect
def log_mission_creation(mission, **kwargs):
    message = "The mission \"%s\" was created." % mission.title
    log_entry(message)


def log_entry(message):
    log_entry = LogEntry(message)
    db.session.add(log_entry)
    db.session.commit()
