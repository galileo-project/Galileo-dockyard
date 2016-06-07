from dockyard.service.interface import BaseHandler
from dockyard.utils.wrapper import auth_manager
from tornado.gen import coroutine
from dockyard.var import GLOBAL

class ApiSysHandeler(BaseHandler):
    @auth_manager
    @coroutine
    def get(self, path=None):
        if   path == "logs":        yield self.get_sys_logs()
        elif path == "settings":    yield self.get_sys_settings()

    @auth_manager
    @coroutine
    def post(self, path=None):
        if path ==  "settings":     yield self.save_sys_settigns()

    @coroutine
    def save_sys_settigns(self):
        self.parse_arg_str("github_client_secret",  False)
        self.parse_arg_str("github_redirect_uri",   False)
        self.parse_arg_str("github_client_id",      False)

        ret_uri = GLOBAL.system.set_github_redirect_uri(self.data["github_redirect_uri"])
        ret_id = GLOBAL.system.set_github_client_id(self.data["github_client_id"])
        ret_secret = GLOBAL.system.set_github_client_secret(self.data["github_client_secret"])

        for ret in [ret_uri, ret_id, ret_secret]:
            if ret[0]:
                return self.return_driver(ret)
        return self.success()

    @coroutine
    def get_sys_settings(self):
        return self.return_driver(GLOBAL.system.settings)

    @coroutine
    def get_sys_logs(self):
        ret = GLOBAL.system.get_logs()
        self.return_driver(ret)