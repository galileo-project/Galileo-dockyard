from dockyard.service.interface.default._handler import DefaultHandeler
from dockyard.var import GLOBAL

routes = [(r"/(.*)",                DefaultHandeler)]

GLOBAL.routes.extend(routes)