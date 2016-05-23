from dockyard.utils.driver import Driver
from dockyard.driver.app._model.build import Build


class BuildDriver(Driver, Build):
    def get_logs(self):
        pass

    def del_build_by_id(self):
        pass

    def del_builds_by_app(self):
        pass

    def get_builds_by_app(self):
        pass

    def get_build_by_app(self):
        pass
