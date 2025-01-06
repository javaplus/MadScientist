class Event:
    def __init__(self):
        self.handlers = []

    ## Add the functions to call when the event fires.
    def subscribe(self, handler):
        self.handlers.append(handler)

    def unsubscribe(self, handler):
        self.handlers.remove(handler)
        
    def reset(self):
        self.handlers = []

    def fire(self, *args, **kwargs):
        for handler in self.handlers:
            handler(*args, **kwargs)