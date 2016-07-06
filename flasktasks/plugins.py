import pkg_resources
import os
import jinja2
from flasktasks import app


plugins = []


def load_plugins():
    templates_loader = [app.jinja_loader]
    for entry_point in pkg_resources.iter_entry_points('flasktasks.plugin'):
        plugin_module = entry_point.load()
        plugin_path = os.path.join(os.path.dirname(plugin_module.__file__),
                                   'templates' )

        templates_loader.append(jinja2.FileSystemLoader(plugin_path))
        plugins.append(plugin_module)
    app.jinja_loader = jinja2.ChoiceLoader(templates_loader)


def dispatch(function, *args, **kwargs):
    return_values = []
    available_plugins = [p for p in plugins if hasattr(p, function)]
    for plugin in available_plugins:
        func = getattr(plugin, function)
        return_values.append(func(*args, **kwargs))
    return return_values
