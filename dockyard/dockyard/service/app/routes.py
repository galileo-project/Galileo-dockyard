from dockyard.var import GLOBAL
from dockyard.service.app._handler import ApiUserAppHandeler

routes = [(r"/api/app/?(.*)",           ApiUserAppHandeler),]

GLOBAL.routes.extend(routes)