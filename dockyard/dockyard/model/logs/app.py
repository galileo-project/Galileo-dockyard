from dockyard.utils.mongo import Mongo
from dockyard.model.logs import Log

class AppLog(Mongo, Log):
    def __init__(self, origin = None):
        self._origin = origin
        Mongo.__init__(self)