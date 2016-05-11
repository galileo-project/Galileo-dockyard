from dockyard.handler import BaseHandler
from dockyard.const.status import APIStatus
from dockyard.utils.wrapper import auth
from dockyard.model.sys.settings import SysSettings
from dockyard.utils.github import GitHubClient
from tornado.gen import coroutine

class PublicGitHubHandeler(BaseHandler):
    @coroutine
    def get(self, path, *args, **kwargs):
        if   path == "list":  self.get_repos()
        elif path == "auth":  self.authorize()

    def authorize(self):
        self.parse_arg_str("code", must=True)
        self.parse_arg_str("state", must=True)

        sys_settings = SysSettings()

        github_redirect_uri  = sys_settings["github_redirect_uri"]
        github_client_id     = sys_settings["github_client_id"]
        github_client_secret = sys_settings["github_client_secret"]

        github_oauth = GitHubClient().oauth

        ret =github_oauth.access_token(github_client_id, github_client_secret, self.data["code"],
                                       github_redirect_uri, self.data["state"])

        self.user["github_access_token"] = ret["access_token"]
        self.user["github_scope"]        = ret["scope"]
        self.user["github_token_type"]   = ret["token_type"]

        self.success()