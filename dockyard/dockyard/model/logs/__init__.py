from dockyard.utils.mongo import Mongo
from dockyard.var import GLOBAL

class Log(Mongo):
    LEVEL  = "level"
    MSG    = "msg"
    ORIGIN = "origin"

    def warn(self, msgs, origin=GLOBAL.SYS_ORIGIN):
        if not isinstance(msgs, list):
            msgs = [msgs]

        for msg in msgs:
            data = {self.LEVEL:     GLOBAL.LOG_WARN,
                    self.MSG:       msg,
                    self.ORIGIN:    origin}
            self.append(data)
        self.flush()

    def fatal(self, msgs, origin=GLOBAL.SYS_ORIGIN):
        if not isinstance(msgs, list):
            msgs = [msgs]

        for msg in msgs:
            data = {self.LEVEL:     GLOBAL.LOG_FATAL,
                    self.MSG:       msg,
                    self.ORIGIN:    origin}
            self.append(data)
        self.flush()

    def puts(self, msgs, origin=GLOBAL.SYS_ORIGIN):
        if not isinstance(msgs, list):
            msgs = [msgs]

        for msg in msgs:
            data = {self.LEVEL:     GLOBAL.LOG_PUTS,
                    self.MSG:       msg,
                    self.ORIGIN:    origin}
            self.append(data)
        self.flush()

    def success(self, msgs, origin=GLOBAL.SYS_ORIGIN):
        if not isinstance(msgs, list):
            msgs = [msgs]

        for msg in msgs:
            data = {self.LEVEL:     GLOBAL.LOG_SUCCESS,
                    self.MSG:       msg,
                    self.ORIGIN:    origin}
            self.append(data)
        self.flush()

    def error(self, msgs, origin=GLOBAL.SYS_ORIGIN):
        if not isinstance(msgs, list):
            msgs = [msgs]

        for msg in msgs:
            data = {self.LEVEL:     GLOBAL.LOG_ERROR,
                    self.MSG:       msg,
                    self.ORIGIN:    origin}
            self.append(data)
        self.flush()