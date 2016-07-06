from flask import Markup
from flasktasks import app
from flasktasks.plugins import dispatch


@app.template_filter('html_dispatch')
def html_dispatch(mission, function):
    values = dispatch(function, mission)
    return Markup(''.join(values))
