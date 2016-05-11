from dockyard.handler import BaseHandler
from dockyard.const.status import APIStatus
from dockyard.utils.wrapper import auth
from dockyard.utils.github import GitHubClient
from tornado.gen import coroutine

class ApiUserGitHubHandeler(BaseHandler):
    @coroutine
    @auth
    def get(self, path, *args, **kwargs):
        if path == "list":  return self.get_apps()

    def get_repos(self):
        github = GitHubClient()

        repos = github.get_repos()