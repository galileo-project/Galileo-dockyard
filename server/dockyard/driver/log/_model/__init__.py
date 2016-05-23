from dockyard.var import GLOBAL

from server.dockyard.utils import Mongo


class Log(Mongo):
    """
    _id
    level
    msg
    origin
    """
    LEVEL  = "level"
    MSG    = "msg"
    ORIGIN = "origin"

    def _warn(self, msgs, origin):
        self.__save(msgs, GLOBAL.LOG_WARN, origin)

    def _fatal(self, msgs, origin):
        self.__save(msgs, GLOBAL.LOG_FATAL, origin)

    def _info(self, msgs, origin):
        self.__save(msgs, GLOBAL.LOG_INFO, origin)

    def _success(self, msgs, origin):
        self.__save(msgs, GLOBAL.LOG_SUCCESS, origin)

    def _error(self, msgs, origin):
        self.__save(msgs, GLOBAL.LOG_ERROR, origin)

    def __save(self, msgs, level, origin):
        if not isinstance(msgs, list):
            msgs = [msgs]

        for msg in msgs:
            data = {self.LEVEL:     level,
                    self.MSG:       msg,
                    self.ORIGIN:    origin or GLOBAL.SYS_ORIGIN}
            self.append(data)
        self.flush()