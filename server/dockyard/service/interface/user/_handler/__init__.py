from dockyard.utils import encrypt
from dockyard.service.interface import BaseHandler
from dockyard.utils.wrapper import auth
from tornado.gen import coroutine
from dockyard.const import APIStatus


class ApiUserHandeler(BaseHandler):
    @auth
    @coroutine
    def get(self, *args, **kwargs):
        self.success(self.user.get_raw())

    @coroutine
    def post(self, *args, **kwargs):
        self.parse_arg_str("user_name",     True)
        self.parse_arg_str("user_pwd",      True)
        self.parse_arg_str("user_email",    True)

        self.user["user_email"] = self.data["user_email"]
        self.user["user_name"]  = self.data["user_name"]
        self.user["user_pwd"]   = encrypt(self.data["user_pwd"])

        if self.user:
            self.user.clear()
            return self.error(APIStatus["STAT_API_USER_EXIST"])

        self.set_user_cookie()
        return self.success(self.user.get_raw())

    @auth
    @coroutine
    def put(self, *args, **kwargs):
        self.parse_arg_str("user_pwd", False)

        if self.user:
            if self.data["user_pwd"]:
                self.user["user_pwd"] = encrypt(self.data["user_pwd"])
        else:
            return self.error(APIStatus["STAT_API_USER_UNEXIST"])

        return self.success(self.user.get_raw())

    @auth
    @coroutine
    def delete(self, *args, **kwargs):
        self.user.remove()
        return self.success()