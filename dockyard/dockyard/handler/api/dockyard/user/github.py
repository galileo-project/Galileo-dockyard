from dockyard.handler import BaseHandler
from dockyard.const.status import APIStatus
from dockyard.utils.wrapper import auth
from dockyard.var import GLOBAL
from dockyard.utils import gen_random
from dockyard.model.sys.settings import SysSettings
from tornado.gen import coroutine

class ApiUserGitHubHandeler(BaseHandler):
    @coroutine
    @auth
    def get(self, path, *args, **kwargs):
        if path == "list":  return self.get_repos()

    def get_repos(self):
        repos = self.user.github.get_repos()
        self.success(repos)

    def github_oauth(self):
        state = gen_random()
        sys_settings = SysSettings()

        github_client_id = sys_settings["github_client_id"]
        self.user.github.oauth.authorize(github_client_id,
                                         GLOBAL.GITHUB_OAUTH_REDIRECT, state)

        return self.success()