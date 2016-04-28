from dockyard.handler import BaseHandler
from dockyard.const import APIStatus
from dockyard.utils import encrypt
from tornado.gen import coroutine

class ApiAuthHandeler(BaseHandler):
    @coroutine
    def post(self, *args, **kwargs):
        self.parse_arg_str("user_name")
        self.parse_arg_str("user_pwd")

        self.user["user_name"] = self.data["user_name"]

        if not self.user:
            return self.error(APIStatus["STAT_API_USER_UNEXIST"])
        if self.user["user_pwd"] != encrypt(self.data["user_pwd"]):
            return self.error(APIStatus["STAT_API_USER_PWD_ERR"])

        self.set_secure_cookie("user", self.user.str_id)
        self.success()