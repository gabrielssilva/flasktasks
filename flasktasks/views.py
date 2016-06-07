from flask import render_template, request, redirect, url_for
from flasktasks import app, db
from flasktasks.models import Mission 


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
    print(request.args)
    return redirect(url_for('missions'))
