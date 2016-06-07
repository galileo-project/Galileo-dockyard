from dockyard.var import GLOBAL
from dockyard.service.interface.github._handler import ApiGitHubHandeler
from dockyard.service.interface.github._handler._public import PublicGitHubHandeler

routes = [(r"/api/github/(.*)",        ApiGitHubHandeler),
          (r"/public/github/(.*)",     PublicGitHubHandeler),]

def init():
    GLOBAL.routes.extend(routes)