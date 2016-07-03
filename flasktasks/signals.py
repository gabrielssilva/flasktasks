from blinker import Namespace


flasktasks_signals = Namespace()
task_created = flasktasks_signals.signal('task-created')
mission_created = flasktasks_signals.signal('mission-created')
