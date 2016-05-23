from dockyard.utils.driver import Driver
from dockyard.driver.app import App
from dockyard.var import GLOBAL
from dockyard.utils.github import GitHubClient
from dockyard.driver.user._model import User
from dockyard.const import APIStatus


class UserDriver(Driver, User):
    def __init__(self):
        User.__init__(self)
        self.__github = None

    def get_by_name(self, name):
        self.find_one({"name":  name})
        if self.exists():
            return self.succes(self)
        else:
            return self.err(APIStatus["STAT_API_USER_UNEXIST"])

    def get_apps(self):
        if self.exists():
            err, msg = App().gets_by_user(self)
            if err:
                return self.err(msg)
            else:
                return self.succes(msg)
        else:
            return self.err(APIStatus["STAT_API_USER_UNEXIST"])

    def get_logs(self):
        if self.exists():
            err, msg = GLOBAL.logging.get_logs_by_user(self)
            if err:
                return self.err(msg)
            else:
                return self.succes(msg)
        else:
            return self.err(APIStatus["STAT_API_USER_UNEXIST"])

    def del_user(self):
        self.remove()
        return self.succes()

    @property
    def github(self):
        if self.exists():
            if not self.__github:
                self.__github = GitHubClient(self)
            return self.succes(self.__github)
        else:
            return self.err(APIStatus["STAT_API_USER_UNEXIST"])