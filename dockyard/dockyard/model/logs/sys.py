from dockyard.utils.mongo import Mongo
from dockyard.model.logs import Log

class SysLog(Mongo, Log):
    def __init__(self, origin = "SYSTEM"):
        self._origin = origin
        Mongo.__init__(self)