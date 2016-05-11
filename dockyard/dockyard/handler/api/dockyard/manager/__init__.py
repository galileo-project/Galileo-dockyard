from dockyard.handler import BaseHandler
from dockyard.const.status import APIStatus
from dockyard.model.sys.settings import SysSettings
from tornado.gen import coroutine
from dockyard.utils.wrapper import auth_manager

class ApiSysHandeler(BaseHandler):
    @auth_manager
    @coroutine
    def get(self, *args, **kwargs):
        sys_settings = SysSettings()
        self.success(sys_settings.get_raw())

    @auth_manager
    @coroutine
    def put(self, *args, **kwargs):
        self.parse_arg_str("github_client_secret",  False)
        self.parse_arg_str("github_redirect_uri",   False)
        self.parse_arg_str("github_client_id",      False)

        sys_settings = SysSettings()

        sys_settings["github_redirect_uri"]     = self.data["github_redirect_uri"]
        sys_settings["github_client_id"]        = self.data["github_client_id"]
        sys_settings["github_client_secret"]    = self.data["github_client_secret"]

        return self.success(sys_settings.get_raw())
