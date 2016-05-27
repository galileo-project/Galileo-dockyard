from dockyard.service.interface import BaseHandler
from dockyard.utils.wrapper import auth_manager
from tornado.gen import coroutine
from dockyard.driver.user import User


class ApiUsersHandeler(BaseHandler):
    @auth_manager
    @coroutine
    def get(self, path=None):
        res = User().all()
        return self.return_driver(res)

    @auth_manager
    @coroutine
    def delete(self, path=None):
        self.parse_arg_str("uid", True)

        user = User()
        ret = user.del_user_by_id(self.data["uid"])
        self.return_driver(ret)