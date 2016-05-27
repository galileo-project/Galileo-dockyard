from dockyard.utils.driver import Driver
from dockyard.const import APIStatus
from dockyard.var import GLOBAL
from dockyard.driver.sys._model._settings import System


class SysDriver(Driver, System):
    def get_github_client_id(self):
        if self.exists():
            return self.succes(self["github_client_id"])
        else:
            return self.err(APIStatus["STAT_API_SYS_OBJ_UNEXIST"])

    def get_github_client_secret(self):
        if self.exists():
            return self.succes(self["github_client_secret"])
        else:
            return self.err(APIStatus["STAT_API_SYS_OBJ_UNEXIST"])

    def get_github_redirect_uri(self):
        if self.exists():
            return self.succes(self["github_redirect_uri"])
        else:
            return self.err(APIStatus["STAT_API_SYS_OBJ_UNEXIST"])

    def set_github_client_id(self, client_id):
        if self.exists():
            self["github_redirect_uri"] = client_id
            return self.succes()
        else:
            return self.err(APIStatus["STAT_API_SYS_OBJ_UNEXIST"])

    def set_github_client_secret(self, client_secret):
        if self.exists():
            self["github_client_secret"] = client_secret
            return self.succes()
        else:
            return self.err(APIStatus["STAT_API_SYS_OBJ_UNEXIST"])

    def set_github_redirect_uri(self, uri):
        if self.exists():
            self["github_redirect_uri"] = uri
            return self.succes()
        else:
            return self.err(APIStatus["STAT_API_SYS_OBJ_UNEXIST"])

    def get_logs(self):
        if self.exists():
            err, msg = GLOBAL.logging.gets_sys_log()
            if err:
                return self.err(msg)
            else:
                return self.succes(msg)
        else:
            return self.err(APIStatus["STAT_API_SYS_OBJ_UNEXIST"])

    @property
    def settings(self):
        if self.exists():
            return self.succes(self.raw)
        else:
            return self.err(APIStatus["STAT_API_SYS_OBJ_UNEXIST"])