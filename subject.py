from .observer import Observer

class Subject:
    def __init__(self):
        self._observers = {}

    def attach(self, event_name, observer: Observer):
        if event_name not in self._observers:
            self._observers[event_name] = []
        self._observers[event_name].append(observer)

    def detach(self, event_name, observer: Observer):
        if event_name in self._observers:
            self._observers[event_name].remove(observer)

    def notify(self, event_name, data=None):
        if event_name in self._observers:
            for observer in self._observers[event_name]:
                observer.update(event_name, data)
