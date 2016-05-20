from dockyard.utils.handler import BaseHandler
from dockyard.const import APIStatus
from dockyard.utils import encrypt
from tornado.gen import coroutine

class ApiAuthHandeler(BaseHandler):
    @coroutine
    def post(self, path):
        if path == "login":     self.login()

    @coroutine
    def get(self, path):
        pass

    @coroutine
    def delete(self, path):
        if path == "logout":    self.logout()

    def login(self):
        self.parse_arg_str("user_name", True)
        self.parse_arg_str("user_pwd",  True)

        self.user["user_name"] = self.data["user_name"]

        if not self.user:
            return self.error(APIStatus["STAT_API_USER_UNEXIST"])
        if self.user["user_pwd"] != encrypt(self.data["user_pwd"]):
            return self.error(APIStatus["STAT_API_USER_PWD_ERR"])

        self.set_user_cookie()
        self.success()

    def logout(self):
        self.del_user_cookie()
        self.success()