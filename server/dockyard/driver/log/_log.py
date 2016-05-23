from dockyard.driver.log._model import Log
from dockyard.utils.driver import Driver
from dockyard.const import APIStatus


class DriverLog(Driver, Log):
    def error(self, msgs, origin):
        self._error(msgs, origin)
        return self.succes()

    def warn(self, msgs, origin):
        self._warn(msgs, origin)
        return self.succes()

    def fatal(self, msgs, origin):
        self._fatal(msgs, origin)
        return self.succes()

    def success(self, msgs, origin):
        self._success(msgs, origin)
        return self.succes()

    def info(self, msgs, origin):
        self._info(msgs, origin)
        return self.succes()

    def get_logs_by_build(self, build):
        self.find({"origin":    build.id})

        if self.exists():
            return self.succes(self)
        else:
            return self.err(APIStatus["STAT_API_LOG_UNEXIST"])

    def get_logs_by_user(self, user):
        self.find({"origin":    user.id})

        if self.exists():
            return self.succes(self)
        else:
            return self.err(APIStatus["STAT_API_LOG_UNEXIST"])