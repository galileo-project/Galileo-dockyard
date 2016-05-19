from dockyard.handler import BaseHandler
from dockyard.const import APIStatus
from dockyard.utils import encrypt
from tornado.gen import coroutine
from dockyard.utils.wrapper import auth_manager

class ApiAuthHandeler(BaseHandler):
    @coroutine
    def post(self, path):
        if path == "login":     self.login()

    @auth_manager
    @coroutine
    def delete(self, path):
        if path == "logout":    self.logout()

    def login(self):
        self.parse_arg_str("manager_name", True)
        self.parse_arg_str("manager_pwd",  True)

        self.user["manager_name"] = self.data["manager_name"]

        if not self.manager:
            return self.error(APIStatus["STAT_API_MANAGER_UNEXIST"])
        if self.user["manager_pwd"] != encrypt(self.data["manager_pwd"]):
            return self.error(APIStatus["STAT_API_MANAGER_PWD_ERR"])

        self.set_manager_cookie()
        self.success()

    def logout(self):
        self.del_manager_cookie()
        self.success()