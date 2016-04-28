from dockyard.handler import BaseHandler
from dockyard.const.status import APIStatus
from dockyard.utils.wrapper import auth
from dockyard.utils import encrypt
from tornado.gen import coroutine

class ApiUserHandeler(BaseHandler):
    @auth
    @coroutine
    def get(self, *args, **kwargs):
        self.success(self.user.get_raw())

    @coroutine
    def post(self, *args, **kwargs):
        self.parse_arg_str("user_name")
        self.parse_arg_str("user_pwd")
        self.parse_arg_str("user_email")

        self.user["user_email"] = self.data["user_email"]
        self.user["user_name"]  = self.data["user_name"]
        self.user["user_pwd"]   = encrypt(self.data["user_pwd"])

        if self.user:
            self.user.clear()
            return self.error(APIStatus["STAT_API_USER_EXIST"])

        return self.success(self.user.get_raw())

    @auth
    @coroutine
    def put(self, *args, **kwargs):
        self.parse_arg_str("user_pwd")

        if not self.data["user_pwd"]:
            return self.error(APIStatus["STAT_API_PWD_EMPTY"])

        if self.user:
            self.user["user_pwd"]  = encrypt(self.data["user_pwd"])
        else:
            return self.error(APIStatus["STAT_API_USER_UNEXIST"])

        return self.success(self.user.get_raw())

    @auth
    @coroutine
    def delete(self, *args, **kwargs):
        self.user.remove()
        return self.success()