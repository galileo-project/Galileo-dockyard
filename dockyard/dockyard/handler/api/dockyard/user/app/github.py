from dockyard.handler import BaseHandler
from dockyard.const.status import APIStatus
from dockyard.utils.wrapper import auth
from pyos.pygit import GitHubClient
from tornado.gen import coroutine

class ApiAppGitHubHandeler(BaseHandler):
    @coroutine
    @auth
    def get(self, path, *args, **kwargs):
        if path == "list":  return self.get_apps()

    def get_apps(self):
        github = GitHubClient(self.user["github_name"], self.user["github_pwd"])

        repos = github.get_repos()