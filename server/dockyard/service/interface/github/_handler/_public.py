from dockyard.service.interface import BaseHandler
from tornado.gen import coroutine
from dockyard.var import GLOBAL


class PublicGitHubHandeler(BaseHandler):
    @coroutine
    def get(self, path, *args, **kwargs):
        if   path == "auth":    self.authorize()

    def authorize(self):
        self.parse_arg_str("code",  must=True)
        self.parse_arg_str("state", must=True)

        github_redirect_uri  = GLOBAL.system["github_redirect_uri"]
        github_client_id     = GLOBAL.system["github_client_id"]
        github_client_secret = GLOBAL.system["github_client_secret"]

        ret = self.user.github.oauth.access_token(github_client_id, github_client_secret,
                                                  self.data["code"], github_redirect_uri, self.data["state"])

        self.user["github_access_token"] = ret["access_token"]
        self.user["github_scope"]        = ret["scope"]
        self.user["github_token_type"]   = ret["token_type"]

        self.redirect("/")