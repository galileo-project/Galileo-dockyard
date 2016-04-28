from dockyard.utils.mongo import Mongo
from dockyard.const import LOG_WARN, LOG_SUCCESS, \
     LOG_FATAL, LOG_ERROR, LOG_PUT, LOG_LEVEL, SYS_ORIGIN

class Log(Mongo):
    LEVEL  = "level"
    MSG    = "msg"
    ORIGIN = "origin"

    def warn(self, msg, origin = SYS_ORIGIN):
        self[self.LEVEL]  = LOG_LEVEL[LOG_WARN]
        self[self.MSG]    = msg
        self[self.ORIGIN] = origin

    def fatal(self, msg, origin = SYS_ORIGIN):
        self[self.LEVEL]  = LOG_LEVEL[LOG_FATAL]
        self[self.MSG]    = msg
        self[self.ORIGIN] = origin

    def put(self, msg, origin = SYS_ORIGIN):
        self[self.LEVEL]  = LOG_LEVEL[LOG_PUT]
        self[self.MSG]    = msg
        self[self.ORIGIN] = origin

    def success(self, msg, origin = SYS_ORIGIN):
        self[self.LEVEL]  = LOG_LEVEL[LOG_SUCCESS]
        self[self.MSG]    = msg
        self[self.ORIGIN] = origin

    def error(self, msg, origin = SYS_ORIGIN):
        self[self.LEVEL]  = LOG_LEVEL[LOG_ERROR]
        self[self.MSG]    = msg
        self[self.ORIGIN] = origin
