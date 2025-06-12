from .subject import Subject
from .persistence import save_event, load_event

_global_subject = Subject()

def register(event_name, observer):
    _global_subject.attach(event_name, observer)

def unregister(event_name, observer):
    _global_subject.detach(event_name, observer)

def notify(event_name, data=None, persist=False):
    if persist:
        save_event(event_name, data)
    _global_subject.notify(event_name, data)

def recover(event_name):
    return load_event(event_name)
