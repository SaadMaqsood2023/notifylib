# Base Observer interface
class Observer:
    def update(self, event_name, data):
        raise NotImplementedError("Observer subclasses must implement the update method.")
