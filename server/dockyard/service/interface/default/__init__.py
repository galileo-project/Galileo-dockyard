from dockyard.var import GLOBAL

from server.dockyard.service.interface.default import DefaultHandeler

routes = [(r"/(.*)",                DefaultHandeler)]

GLOBAL.routes.extend(routes)