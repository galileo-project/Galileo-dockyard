from dockyard.var import GLOBAL
from dockyard.service.interface.default._handler import DefaultHandeler

routes = [(r"/(.*)",                DefaultHandeler)]

GLOBAL.routes.extend(routes)