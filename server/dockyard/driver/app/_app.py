from dockyard.utils.driver import Driver
from dockyard.driver.app._model import App
from dockyard.const import APIStatus
from dockyard.driver.app._build import BuildDriver
from dockyard.var import GLOBAL
from dockyard.utils.wrapper import exists

class AppDriver(Driver, App):
    def gets_by_user(self, user):
        self.find({"user_id": user.id})

        if self.exists():
            return self.succes(self)
        else:
            return self.err(APIStatus["STAT_API_APP_UNEXIST"])

    @exists(APIStatus["STAT_API_APP_UNEXIST"])
    def get_latest_build(self):
        err, msg = BuildDriver().get_latest_build_by_app(self)
        if err:
            return self.err(msg)
        else:
            return self.succes(msg)

    @exists(APIStatus["STAT_API_APP_UNEXIST"])
    def get_builds(self):
        err, msg = BuildDriver().get_builds_by_app(self)
        if err:
            return self.err(msg)
        else:
            return self.succes(msg)

    def del_app_by_id(self, _id):
        self.get_by_id(_id)
        return self.__remove()

    def del_apps_by_user(self, user):
        self.gets_by_user(user)
        return self.__remove()

    @exists(APIStatus["STAT_API_APP_UNEXIST"])
    def build(self):
        self["build_times"] += 1
        return BuildDriver().add(self)

    def add(self, user, app_github):
        self["user"]        = user.id
        self["build_times"] = 0

    @exists(APIStatus["STAT_API_APP_UNEXIST"])
    def update(self, app_github):
        pass

    @exists(APIStatus["STAT_API_APP_UNEXIST"])
    def __remove(self):
        self.remove()
        return self.succes()

    @exists(APIStatus["STAT_API_APP_UNEXIST"])
    def log_err(self, msg):
        GLOBAL.logging.error(msg, self.str_id)
        return self.succes()

    @exists(APIStatus["STAT_API_APP_UNEXIST"])
    def log_info(self, msg):
        GLOBAL.logging.info(msg, self.str_id)
        return self.succes()

    @exists(APIStatus["STAT_API_APP_UNEXIST"])
    def log_success(self, msg):
        GLOBAL.logging.success(msg, self.str_id)
        return self.succes()

    @exists(APIStatus["STAT_API_APP_UNEXIST"])
    def log_warn(self, msg):
        GLOBAL.logging.warn(msg, self.str_id)
        return self.succes()

    @exists(APIStatus["STAT_API_APP_UNEXIST"])
    def log_fatal(self, msg):
        GLOBAL.logging.fatal(msg, self.str_id)
        return self.succes()