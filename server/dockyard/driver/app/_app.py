from dockyard.utils.driver import Driver
from dockyard.driver.app._model import App
from dockyard.const import APIStatus


class AppDriver(Driver, App):
    def gets_by_user(self, user):
        self.find({"user_id": user.id})

        if self.exists():
            return self.succes(self)
        else:
            return self.err(APIStatus["STAT_API_APP_UNEXIST"])

    def get_latest_build(self):
        pass

    def get_builds(self):
        pass

    def del_app_by_id(self):
        pass

    def del_apps_by_user(self):
        pass
