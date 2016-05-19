from dockyard.var import GLOBAL
from dockyard.service.github._handler import PublicGitHubHandeler

routes = [(r"/api/public/github/(.*)",        PublicGitHubHandeler)]

GLOBAL.routes.extend(routes)