from dockyard.service.interface.github import PublicGitHubHandeler
from dockyard.var import GLOBAL

routes = [(r"/api/public/github/(.*)",        PublicGitHubHandeler)]

GLOBAL.routes.extend(routes)