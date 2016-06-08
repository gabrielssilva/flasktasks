from flask import request
from flasktasks import app

@app.template_filter('is_selected')
def is_mission_selected(mission_id):
    if str(mission_id) == request.args.get('mission_id'):
        return "selected"
    else:
        return ''

@app.template_filter('is_current_page')
def is_current_page(current_path):
    if current_path == request.path:
        return "active"
    else:
        return ''

@app.template_filter('human')
def str_to_title(str_val):
    return str_val.title()
