from dockyard.utils.request import Request


class GitHubClient:
    class __Oauth:
        AUTH_URL         = "https://github.com/login/oauth/authorize"
        ACCESS_TOKEN_URL = "https://github.com/login/oauth/access_token"

        def __init__(self, request=None):
            self.__request = request or Request()

        def authorize(self, client_id, redirect_uri, state, scope="read:org", allow_signup="true"):
            data = {"client_id":    client_id,
                    "redirect_uri": redirect_uri,
                    "state":        state,
                    "scope":        scope,
                    "allow_signup": allow_signup}
            return self.__request.get(self.AUTH_URL, data)

        def access_token(self, client_id, client_secret, code, redirect_uri, state):
            data = {"client_id":        client_id,
                    "client_secret":    client_secret,
                    "code":             code,
                    "redirect_uri":     redirect_uri,
                    "state":            state}

            return self.__request.post(self.ACCESS_TOKEN_URL, data)

    def __init__(self):
        self.__request = Request()
        self.__oauth = None

        self.__request.set_header({"Accept": "application/json"})

    @property
    def oauth(self):
        if not self.__oauth:
            self.__oauth = self.__Oauth(self.__request)
        return self.__oauth

    def get_repos(self):
        pass

    def get_orgs(self):
        pass