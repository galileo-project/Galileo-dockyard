from dockyard.handler import BaseHandler
from dockyard.const.status import APIStatus
from dockyard.utils.wrapper import auth
from tornado.gen import coroutine

class ApiUserSettingsHandeler(BaseHandler):
    @auth
    @coroutine
    def put(self, *args, **kwargs):
        self.parse_arg_str("github_name",   must=False)
        self.parse_arg_str("github_pwd",    must=False)
        self.parse_arg_str("user_email", must=False)

        self.user["github_name"] = self.data["github_name"]
        self.user["github_pwd"]  = self.data["github_pwd"]
        self.user["user_email"]  = self.data["user_email"]

        return self.success(self.user.get_raw())

