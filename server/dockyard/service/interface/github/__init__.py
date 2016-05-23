from dockyard.var import GLOBAL

from server.dockyard.service.interface.github import PublicGitHubHandeler

routes = [(r"/api/public/github/(.*)",        PublicGitHubHandeler)]

GLOBAL.routes.extend(routes)