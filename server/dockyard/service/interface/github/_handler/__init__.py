from dockyard.service.interface import BaseHandler
from tornado.gen import coroutine
from dockyard.var import GLOBAL
from dockyard.utils import gen_random


class ApiGitHubHandeler(BaseHandler):
    @coroutine
    def get(self, path, *args, **kwargs):
        if   path == "auth":    self.authorize()
        elif path == "oauth":   self.get_oauth()

    def authorize(self):
        self.parse_arg_str("code",  must=True)
        self.parse_arg_str("state", must=True)

        err, github_redirect_uri  = GLOBAL.system.get_github_redirect_uri()
        err, github_client_id     = GLOBAL.system.get_github_client_id()
        err, github_client_secret = GLOBAL.system.get_github_client_secret()

        ret = self.user.github.oauth.access_token(github_client_id, github_client_secret,
                                                  self.data["code"], github_redirect_uri,
                                                  self.data["state"])

        self.user["github_access_token"] = ret["access_token"]
        self.user["github_scope"]        = ret["scope"]
        self.user["github_token_type"]   = ret["token_type"]

        return self.success()

    def get_oauth(self):
        err, client_id      = GLOBAL.system.get_github_client_id()
        err, redirect_uri   = GLOBAL.system.get_github_redirect_uri()
        scope               = "read:org"
        state               = gen_random(10)
        allow_signup        = True

        url = self.user.github.oauth.authorize(client_id, redirect_uri, state, scope, allow_signup)
        return self.success(url)

    def push_repos(self):
        pass