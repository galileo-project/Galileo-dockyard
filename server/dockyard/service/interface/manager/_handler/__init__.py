from dockyard.driver.sys import System
from dockyard.service.interface import BaseHandler
from dockyard.utils.wrapper import auth_manager
from tornado.gen import coroutine


class ApiManagerHandeler(BaseHandler):
    @auth_manager
    @coroutine
    def get(self, *args, **kwargs):
        err, msg = System().settings
        if err:
            return self.error(msg)
        else:
            return self.success(msg)

    @auth_manager
    @coroutine
    def post(self, *args, **kwargs):
        self.parse_arg_str("github_client_secret",  False)
        self.parse_arg_str("github_redirect_uri",   False)
        self.parse_arg_str("github_client_id",      False)

        sys_settings = System()

        sys_settings["github_redirect_uri"]  = self.data["github_redirect_uri"]
        sys_settings["github_client_id"]     = self.data["github_client_id"]
        sys_settings["github_client_secret"] = self.data["github_client_secret"]

        err, msg = sys_settings.settings
        if err:
            return self.error(msg)
        else:
            return self.success(msg)
