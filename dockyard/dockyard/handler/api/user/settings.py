from dockyard.handler import BaseHandler
from dockyard.const.status import APIStatus
from dockyard.utils.wrapper import auth
from tornado.gen import coroutine

class ApiUserSettingsHandeler(BaseHandler):
    @auth
    @coroutine
    def put(self, *args, **kwargs):
        self.parse_arg_str("user_git",   must=False)
        self.parse_arg_str("user_url",   must=False)
        self.parse_arg_str("user_email", must=False)

        self.user["user_git"]   = self.data["user_git"]
        self.user["user_url"]   = self.data["user_url"]
        self.user["user_email"] = self.data["user_email"]

        return self.success(self.user.get_raw())

