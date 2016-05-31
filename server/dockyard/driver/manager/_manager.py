from dockyard.utils.driver import Driver
from dockyard.driver.manager._model import Manager
from dockyard.driver.user import User
from dockyard.const import APIStatus
from dockyard.utils import encrypt
from dockyard.utils.wrapper import exists


class ManagerDriver(Driver, Manager):
    def get_users(self):
        users = User().all()
        if users.exists():
            return self.succes(users)
        else:
            return self.err(APIStatus["STAT_API_USER_UNEXIST"])

    def verify(self, name, pwd):
        self.find_one({"name": name})

        if self.exists():
            if self["password"] == encrypt(pwd):
                return self.succes()
            else:
                return self.err(APIStatus["STAT_API_MANAGER_PWD_ERR"])
        else:
            return self.err(APIStatus["STAT_API_MANAGER_UNEXIST"])

    @exists(APIStatus["STAT_API_MANAGER_UNEXIST"])
    def update_pwd(self, pwd):
        self["password"] = encrypt(pwd)
        return self.succes()

    def del_user_by_uid(self, uid):
        user = User().get_by_id(uid)

        if user.exists():
            user.remove()
            return self.succes()
        else:
            return self.err(APIStatus["STAT_API_USER_UNEXIST"])

    def add(self, name, password):
        self.find_one({"name": name})

        if self.exists():
            return self.err(APIStatus["STAT_API_MANAGER_EXIST"])

        self["name"]     = name
        self["password"] = encrypt(password)
        return self.succes()