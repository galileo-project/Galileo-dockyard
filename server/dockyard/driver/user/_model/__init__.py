from dockyard.model.user.app import UserApp
from dockyard.var import GLOBAL

from server.dockyard.utils import GitHubClient
from server.dockyard.utils import Mongo


class User(Mongo):
    def __init__(self):
        Mongo.__init__(self)
        self.__github = None
        self.__app    = None

    def get_by_id(self, _id):
        return self.find_one({GLOBAL.MID: _id})

    @property
    def github(self):
        if not self.__github:
            self.__github = GitHubClient(self)
        return self.__github

    @property
    def app(self):
        if not self.__app:
            self.__app = UserApp(self)
        return self.__app