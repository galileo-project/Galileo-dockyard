from dockyard.var import GLOBAL
from dockyard.service.interface.github._handler import PublicGitHubHandeler

routes = [(r"/api/public/github/(.*)",        PublicGitHubHandeler)]

def init():
    GLOBAL.routes.extend(routes)