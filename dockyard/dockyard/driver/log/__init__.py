from dockyard.utils.driver import Driver
from dockyard.driver.log._model import Log

class DriverLog(Driver, Log):
    def error(self, msgs, origin):
        self._error(msgs, origin)

    def warn(self, msgs, origin):
        self._warn(msgs, origin)

    def fatal(self, msgs, origin):
        self._fatal(msgs, origin)

    def success(self, msgs, origin):
        self._success(msgs, origin)

    def info(self, msgs, origin):
        self._info(msgs, origin)

    def get_logs_by_build(self):
        pass

    def get_logs_by_user(self):
        pass