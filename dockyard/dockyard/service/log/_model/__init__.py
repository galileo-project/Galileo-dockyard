from dockyard.utils.mongo import Mongo
from dockyard.var import GLOBAL

class Log(Mongo):
    LEVEL  = "level"
    MSG    = "msg"
    ORIGIN = "origin"

    def __init__(self):
        Mongo.__init__(self)
        self.__origin = GLOBAL.SYS_ORIGIN

    def set_origin(self, origin):
        self.__origin = origin

    def warn(self, msgs):
        if not isinstance(msgs, list):
            msgs = [msgs]

        for msg in msgs:
            data = {self.LEVEL:     GLOBAL.LOG_WARN,
                    self.MSG:       msg,
                    self.ORIGIN:    self.__origin}
            self.append(data)
        self.flush()

    def fatal(self, msgs):
        if not isinstance(msgs, list):
            msgs = [msgs]

        for msg in msgs:
            data = {self.LEVEL:     GLOBAL.LOG_FATAL,
                    self.MSG:       msg,
                    self.ORIGIN:    self.__origin}
            self.append(data)
        self.flush()

    def puts(self, msgs):
        if not isinstance(msgs, list):
            msgs = [msgs]

        for msg in msgs:
            data = {self.LEVEL:     GLOBAL.LOG_PUTS,
                    self.MSG:       msg,
                    self.ORIGIN:    self.__origin}
            self.append(data)
        self.flush()

    def success(self, msgs):
        if not isinstance(msgs, list):
            msgs = [msgs]

        for msg in msgs:
            data = {self.LEVEL:     GLOBAL.LOG_SUCCESS,
                    self.MSG:       msg,
                    self.ORIGIN:    self.__origin}
            self.append(data)
        self.flush()

    def error(self, msgs):
        if not isinstance(msgs, list):
            msgs = [msgs]

        for msg in msgs:
            data = {self.LEVEL:     GLOBAL.LOG_ERROR,
                    self.MSG:       msg,
                    self.ORIGIN:    self.__origin}
            self.append(data)
        self.flush()