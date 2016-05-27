from dockyard.utils.driver import Driver
from dockyard.driver.app import App
from dockyard.var import GLOBAL
from dockyard.utils.github import GitHubClient
from dockyard.driver.user._model import User
from dockyard.const import APIStatus
from dockyard.utils import encrypt


class UserDriver(Driver, User):
    def __init__(self):
        User.__init__(self)
        self.__github = None

    def add(self, name, email, password):
        self.find_one({"email": email})
        if self.exists():
            return self.err(APIStatus["STAT_API_USER_EXIST"])

        self["name"]     = name
        self["email"]    = email
        self["password"] = encrypt(password)
        return self.succes()

    def verify(self, pwd):
        if self.exists():
            if self["password"] == encrypt(pwd):
                return self.succes()
            else:
                return self.err(APIStatus["STAT_API_USER_PWD_ERR"])
        else:
            return self.err(APIStatus["STAT_API_USER_UNEXIST"])

    def get_by_email(self, email):
        self.find_one({"email":  email})
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
        if self.exists():
            self.remove()
            return self.succes()
        else:
            return self.err(APIStatus["STAT_API_USER_UNEXIST"])

    def del_user_by_id(self, _id):
        self.get_by_id(_id)
        print(self.exists())
        return self.del_user()

    @property
    def github(self):
        if self.exists():
            if not self.__github:
                self.__github = GitHubClient(self)
            return self.succes(self.__github)
        else:
            return self.err(APIStatus["STAT_API_USER_UNEXIST"])

    def all(self, skip=None, limit=None, order=None):
        User.all(self, skip, limit, order)
        return self.succes(self.raw)

    def update_password(self, password):
        if self.exists():
            self["password"] = encrypt(password)
            return self.succes()
        else:
            return self.err(APIStatus["STAT_API_USER_UNEXIST"])
