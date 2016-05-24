from dockyard.utils.driver import Driver
from dockyard.driver.app._model.build import Build
from dockyard.const import APIStatus
from dockyard.var import GLOBAL
import time


class BuildDriver(Driver, Build):
    def get_logs(self):
        if self.exists():
            err, msg = GLOBAL.logging.get_logs_by_build(self)
            if err:
                return self.err(msg)
            else:
                return self.succes(msg)
        else:
            return self.err(APIStatus["STAT_API_BUILD_UNEXIST"])

    def get_builds_by_app(self, app):
        self.find({"app_id": app.id})

        if self.exists():
            return self.succes(self)
        else:
            return self.err(APIStatus["STAT_API_BUILD_UNEXIST"])

    def get_latest_build_by_app(self, app):
        self.find_one({"app_id":    app.id,
                       "build_no":  app["build_times"]})

        if self.exists():
            return self.succes(self)
        else:
            return self.err(APIStatus["STAT_API_BUILD_UNEXIST"])

    def del_build_by_id(self, _id):
        self.get_by_id(_id)

        if self.exists():
            self.remove()
            return self.succes()
        else:
            return self.err(APIStatus["STAT_API_BUILD_UNEXIST"])

    def del_builds_by_app(self, app):
        self.get_builds_by_app(app)

        if self.exists():
            self.remove()
            return self.succes()
        else:
            return self.err(APIStatus["STAT_API_BUILD_UNEXIST"])

    def add(self, app):
        self["app_id"]   = app.id
        self["user_id"]  = app["user_id"]
        self["build_no"] = app["build_times"]
        return self.succes()

    def build(self):
        if self.exists():
            self["timestamp"] = time.time()
            # TODO build
        else:
            return self.err(APIStatus["STAT_API_BUILD_UNEXIST"])
