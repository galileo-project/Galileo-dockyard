from dockyard.utils import encrypt
from dockyard.service.interface import BaseHandler
from dockyard.utils.wrapper import auth
from tornado.gen import coroutine
from dockyard.const import APIStatus


class ApiUserHandeler(BaseHandler):
    @auth
    @coroutine
    def get(self, *args, **kwargs):
        self.success(self.user.raw)

    @coroutine
    def post(self, *args, **kwargs):
        self.parse_arg_str("name",     True)
        self.parse_arg_str("password", True)
        self.parse_arg_str("email",    True)

        ret = self.user.add(self.data["name"], self.data["email"], self.data["password"])

        if not ret[0]:
            self.set_user_cookie()

        return self.return_driver(ret)

    @auth
    @coroutine
    def put(self, *args, **kwargs):
        self.parse_arg_str("password", True)
        ret = self.user.update_password(self.data["password"])
        return self.return_driver(ret)