from dockyard.utils.driver import Driver
from dockyard.driver.sys._model._settings import SysSettings


class SysDriver(Driver, SysSettings):
    def get_github_client_id(self):
        pass

    def get_github_client_secret(self):
        pass

    def get_github_redirect_uri(self):
        pass

    def set_github_client_id(self, client_id):
        pass

    def set_github_client_secret(self, client_secret):
        pass

    def set_github_redirect_uri(self, uri):
        pass

    def get_logs(self):
        pass
