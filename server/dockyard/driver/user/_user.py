from dockyard.utils.driver import Driver
from dockyard.driver.app import App
from dockyard.utils.github import GitHubClient
from dockyard.driver.user._model import User


class UserDriver(Driver, User):
    def __init__(self):
        User.__init__(self)
        self.__github = None
        self.__app    = None

    def get_by_name(self):
        pass

    def get_apps(self):
        pass

    def get_logs(self):
        pass

    def del_user(self):
        pass

    @property
    def github(self):
        if not self.__github:
            self.__github = GitHubClient(self)
        return self.__github

    @property
    def app(self):
        if not self.__app:
            self.__app = App().get_by_user(self)
        return self.__app