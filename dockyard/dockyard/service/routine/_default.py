from dockyard.var import GLOBAL

class _Routine:
    KEY = None

    def __init__(self):
        GLOBAL.mq.subscribe(self.KEY, self)

    def callback(self, msg):
        raise NotImplemented

    def resume(self):
        raise NotImplemented

