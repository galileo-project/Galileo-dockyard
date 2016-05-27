from dockyard.service.interface import BaseHandler
from dockyard.utils.wrapper import auth_manager
from tornado.gen import coroutine


class ApiAuthHandeler(BaseHandler):
    @coroutine
    def post(self, path=None):
        if path == "login":     self.login()

    @auth_manager
    @coroutine
    def delete(self, path):
        if path == "logout":    self.logout()

    def login(self):
        self.parse_arg_str("manager_name", True)
        self.parse_arg_str("manager_pwd",  True)

        err, msg = self.manager.verify(self.data["manager_name"], self.data["manager_pwd"])

        if err:
            return self.error(msg)
        else:
            self.set_manager_cookie()
            self.success()

    def logout(self):
        self.del_manager_cookie()
        self.success()