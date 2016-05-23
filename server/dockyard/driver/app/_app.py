from dockyard.utils.driver import Driver
from dockyard.driver.app._model import App


class AppDriver(Driver, App):
    def get_by_user(self, user):
        pass

    def get_latest_build(self):
        pass

    def get_builds(self):
        pass

    def del_app_by_id(self):
        pass

    def del_apps_by_user(self):
        pass
