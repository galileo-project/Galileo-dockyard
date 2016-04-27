from dockyard.const import LOG_WARN, LOG_SUCCESS, \
     LOG_FATAL, LOG_ERROR, LOG_PUT, LOG_RAW, LOG_LEVEL

class Log:
    LEVEL = "level"
    MSG   = "msg"

    def warn(self, msg):
        self[self.LEVEL] = LOG_LEVEL[LOG_WARN]
        self[self.MSG]   = msg

    def fatal(self, msg):
        self[self.LEVEL] = LOG_LEVEL[LOG_FATAL]
        self[self.MSG]   = msg

    def put(self, msg):
        self[self.LEVEL] = LOG_LEVEL[LOG_PUT]
        self[self.MSG]   = msg

    def success(self, msg):
        self[self.LEVEL] = LOG_LEVEL[LOG_SUCCESS]
        self[self.MSG]   = msg

    def error(self, msg):
        self[self.LEVEL] = LOG_LEVEL[LOG_ERROR]
        self[self.MSG]   = msg
