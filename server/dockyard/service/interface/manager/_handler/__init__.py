from dockyard.service.interface import BaseHandler
from dockyard.utils.wrapper import auth_manager
from tornado.gen import coroutine
from dockyard.var import GLOBAL

class ApiManagerHandeler(BaseHandler):
    @auth_manager
    @coroutine
    def get(self, *args, **kwargs):
        return self.return_driver(GLOBAL.system.settings)

    @auth_manager
    @coroutine
    def post(self, *args, **kwargs):
        self.parse_arg_str("github_client_secret",  False)
        self.parse_arg_str("github_redirect_uri",   False)
        self.parse_arg_str("github_client_id",      False)

        GLOBAL.system["github_redirect_uri"]  = self.data["github_redirect_uri"]
        GLOBAL.system["github_client_id"]     = self.data["github_client_id"]
        GLOBAL.system["github_client_secret"] = self.data["github_client_secret"]

        return self.success()
