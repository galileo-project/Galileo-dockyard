from dockyard.utils.driver import Driver
from dockyard.driver.manager._model import Manager


class ManagerDriver(Driver, Manager):
    def get_users(self):
        pass

    def verify(self, name, pwd):
        pass

    def update_pwd(self):
        pass

    def del_user_by_uid(self, uid):
        pass
