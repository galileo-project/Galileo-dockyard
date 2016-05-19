from dockyard.var import GLOBAL
from dockyard.service.default._handler import DefaultHandeler

routes = [(r"/(.*)",                DefaultHandeler)]

GLOBAL.routes.extend(routes)