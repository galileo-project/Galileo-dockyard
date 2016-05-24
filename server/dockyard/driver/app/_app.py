from dockyard.utils.driver import Driver
from dockyard.driver.app._model import App
from dockyard.const import APIStatus
from dockyard.driver.app._build import BuildDriver

class AppDriver(Driver, App):
    def gets_by_user(self, user):
        self.find({"user_id": user.id})

        if self.exists():
            return self.succes(self)
        else:
            return self.err(APIStatus["STAT_API_APP_UNEXIST"])

    def get_latest_build(self):
        if self.exists():
            err, msg = BuildDriver().get_latest_build_by_app(self)
            if err:
                return self.err(msg)
            else:
                return self.succes(msg)
        else:
            return self.err(APIStatus["STAT_API_APP_UNEXIST"])

    def get_builds(self):
        if self.exists():
            err, msg = BuildDriver().get_builds_by_app(self)
            if err:
                return self.err(msg)
            else:
                return self.succes(msg)
        else:
            return self.err(APIStatus["STAT_API_APP_UNEXIST"])

    def del_app_by_id(self, _id):
        self.get_by_id(_id)
        return self.__remove()

    def del_apps_by_user(self, user):
        self.gets_by_user(user)
        return self.__remove()

    def build(self):
        if self.exists():
            self["build_times"] += 1
            return BuildDriver().add(self)
        else:
            return self.err(APIStatus["STAT_API_APP_UNEXIST"])

    def add(self, user, app_github):
        self["user"]        = user.id
        self["build_times"] = 0

    def update(self, app_github):
        pass

    def __remove(self):
        if self.exists():
            self.remove()
            return self.succes()
        else:
            return self.err(APIStatus["STAT_API_APP_UNEXIST"])
