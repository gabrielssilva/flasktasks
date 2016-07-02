import pkg_resources


plugins = []


def load_plugins():
    for entry_point in pkg_resources.iter_entry_points('flasktasks.plugin'):
        plugins.append(entry_point.load())


def dispatch(function, *args, **kwargs):
    available_plugins = [p for p in plugins if hasattr(p, function)]
    for plugin in available_plugins:
        func = getattr(plugin, function)
        return func(*args, **kwargs)
