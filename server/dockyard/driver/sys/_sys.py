from dockyard.utils.driver import Driver
from dockyard.const import APIStatus
from dockyard.var import GLOBAL
from dockyard.driver.sys._model._settings import System
from dockyard.utils.wrapper import exists


class SysDriver(Driver, System):
    @exists(APIStatus["STAT_API_SYS_OBJ_UNEXIST"])
    def get_github_client_id(self):
        return self.succes(self["github_client_id"])

    @exists(APIStatus["STAT_API_SYS_OBJ_UNEXIST"])
    def get_github_client_secret(self):
        return self.succes(self["github_client_secret"])

    @exists(APIStatus["STAT_API_SYS_OBJ_UNEXIST"])
    def get_github_redirect_uri(self):
        return self.succes(self["github_redirect_uri"])

    @exists(APIStatus["STAT_API_SYS_OBJ_UNEXIST"])
    def set_github_client_id(self, client_id):
        self["github_client_id"] = client_id
        self.flush()
        return self.succes()

    @exists(APIStatus["STAT_API_SYS_OBJ_UNEXIST"])
    def set_github_client_secret(self, client_secret):
        self["github_client_secret"] = client_secret
        self.flush()
        return self.succes()

    @exists(APIStatus["STAT_API_SYS_OBJ_UNEXIST"])
    def set_github_redirect_uri(self, uri):
        self["github_redirect_uri"] = uri
        self.flush()
        return self.succes()

    @exists(APIStatus["STAT_API_SYS_OBJ_UNEXIST"])
    def get_logs(self):
        err, msg = GLOBAL.logging.get_sys_logs()
        if err:
            return self.err(msg)
        else:
            return self.succes(msg)

    @staticmethod
    def log_err(msg):
        GLOBAL.logging.error(msg, GLOBAL.SYS_ORIGIN)

    @staticmethod
    def log_info(msg):
        GLOBAL.logging.info(msg, GLOBAL.SYS_ORIGIN)

    @staticmethod
    def log_success(msg):
        GLOBAL.logging.success(msg, GLOBAL.SYS_ORIGIN)

    @staticmethod
    def log_warn(msg):
        GLOBAL.logging.warn(msg, GLOBAL.SYS_ORIGIN)

    @staticmethod
    def log_fatal(msg):
        GLOBAL.logging.fatal(msg, GLOBAL.SYS_ORIGIN)

    @property
    @exists(APIStatus["STAT_API_SYS_OBJ_UNEXIST"])
    def settings(self):
        return self.succes(self.raw)