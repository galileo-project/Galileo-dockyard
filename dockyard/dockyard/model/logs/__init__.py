from dockyard.utils.mongo import Mongo
from dockyard.const import LOG_WARN, LOG_SUCCESS, \
     LOG_FATAL, LOG_ERROR, LOG_PUTS, LOG_LEVEL, SYS_ORIGIN

class Log(Mongo):
    LEVEL  = "level"
    MSG    = "msg"
    ORIGIN = "origin"

    def warn(self, msgs, origin = SYS_ORIGIN):
        if not isinstance(msgs, list):
            msgs = [msgs]

        for msg in msgs:
            data = {self.LEVEL: LOG_LEVEL[LOG_WARN],
                    self.MSG:     msg,
                    self.ORIGIN: origin}
            self.append(data)
        self.flush()

    def fatal(self, msgs, origin = SYS_ORIGIN):
        if not isinstance(msgs, list):
            msgs = [msgs]

        for msg in msgs:
            data = {self.LEVEL: LOG_LEVEL[LOG_FATAL],
                    self.MSG:     msg,
                    self.ORIGIN: origin}
            self.append(data)
        self.flush()

    def puts(self, msgs, origin = SYS_ORIGIN):
        if not isinstance(msgs, list):
            msgs = [msgs]

        for msg in msgs:
            data = {self.LEVEL: LOG_LEVEL[LOG_PUTS],
                    self.MSG:     msg,
                    self.ORIGIN: origin}
            self.append(data)
        self.flush()

    def success(self, msgs, origin = SYS_ORIGIN):
        if not isinstance(msgs, list):
            msgs = [msgs]

        for msg in msgs:
            data = {self.LEVEL: LOG_LEVEL[LOG_SUCCESS],
                    self.MSG:     msg,
                    self.ORIGIN: origin}
            self.append(data)
        self.flush()

    def error(self, msgs, origin = SYS_ORIGIN):
        if not isinstance(msgs, list):
            msgs = [msgs]

        for msg in msgs:
            data = {self.LEVEL: LOG_LEVEL[LOG_ERROR],
                    self.MSG:     msg,
                    self.ORIGIN: origin}
            self.append(data)
        self.flush()