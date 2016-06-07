from flask import render_template, request, redirect, url_for, abort
from collections import defaultdict
from flasktasks import app, db
from flasktasks.models import Mission, Task, Status 


@app.route('/')
def index():
    return "Hello world"

@app.route('/missions')
def missions():
    missions = Mission.query.all()
    return render_template('mission/index.html', missions=missions)

@app.route('/missions/new', methods=['POST', 'GET'])
def new_mission():
    if request.method == 'POST':
        mission = Mission(request.form.get('title'),
                          request.form.get('description'))
        db.session.add(mission)
        db.session.commit()
        return redirect(url_for('missions'))
    else:
        return render_template('mission/new.html')

@app.route('/tasks')
def tasks():
    tasks = Task.query.all()
    tasks_by_status = defaultdict(list)
    for task in tasks:
        status = Status(task.status).name 
        tasks_by_status[status].append(task)
    return render_template('task/index.html', tasks=tasks_by_status)

@app.route('/tasks/new', methods=['POST', 'GET'])
def new_task():
    if request.method == 'POST':
        task = Task(request.form.get('title'),
                    request.form.get('description'),
                    1)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('tasks'))
    else:
        return render_template('task/new.html')

@app.route('/tasks/<int:task_id>')
def task(task_id):
    task = Task.query.get(task_id)
    if task == None: abort(404)
    return render_template('task/task.html', task=task)

@app.route('/tasks/<int:task_id>/set_status/<status>')
def set_status(task_id, status):
    task = Task.query.get(task_id)
    if task == None: abort(404)
    try:
        task.status = Status[status.upper()].value
    except KeyError:
        abort(400)

    db.session.add(task)
    db.session.commit()
    return redirect(url_for('tasks'))
