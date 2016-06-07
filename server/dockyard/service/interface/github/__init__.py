from dockyard.var import GLOBAL
from dockyard.service.interface.github._handler import ApiGitHubHandeler

routes = [(r"/api/github/(.*)",        ApiGitHubHandeler)]
def init():
    GLOBAL.routes.extend(routes)