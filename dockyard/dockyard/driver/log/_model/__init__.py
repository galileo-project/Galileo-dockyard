from dockyard.utils.mongo import Mongo
from dockyard.var import GLOBAL

class Log(Mongo):
    LEVEL  = "level"
    MSG    = "msg"
    ORIGIN = "origin"

    def __init__(self):
        Mongo.__init__(self)
        self.__origin = GLOBAL.SYS_ORIGIN

    def _warn(self, msgs, origin):
        if not isinstance(msgs, list):
            msgs = [msgs]

        for msg in msgs:
            data = {self.LEVEL:     GLOBAL.LOG_WARN,
                    self.MSG:       msg,
                    self.ORIGIN:    origin or self.__origin}
            self.append(data)
        self.flush()

    def _fatal(self, msgs, origin):
        if not isinstance(msgs, list):
            msgs = [msgs]

        for msg in msgs:
            data = {self.LEVEL:     GLOBAL.LOG_FATAL,
                    self.MSG:       msg,
                    self.ORIGIN:    origin or self.__origin}
            self.append(data)
        self.flush()

    def _info(self, msgs, origin):
        if not isinstance(msgs, list):
            msgs = [msgs]

        for msg in msgs:
            data = {self.LEVEL:     GLOBAL.LOG_INFO,
                    self.MSG:       msg,
                    self.ORIGIN:    origin or self.__origin}
            self.append(data)
        self.flush()

    def _success(self, msgs, origin):
        if not isinstance(msgs, list):
            msgs = [msgs]

        for msg in msgs:
            data = {self.LEVEL:     GLOBAL.LOG_SUCCESS,
                    self.MSG:       msg,
                    self.ORIGIN:    origin or self.__origin}
            self.append(data)
        self.flush()

    def _error(self, msgs, origin):
        if not isinstance(msgs, list):
            msgs = [msgs]

        for msg in msgs:
            data = {self.LEVEL:     GLOBAL.LOG_ERROR,
                    self.MSG:       msg,
                    self.ORIGIN:    origin or self.__origin}
            self.append(data)
        self.flush()