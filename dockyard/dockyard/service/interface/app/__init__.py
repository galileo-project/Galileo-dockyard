from dockyard.service.interface.app._handler import ApiUserAppHandeler
from dockyard.var import GLOBAL

routes = [(r"/api/app/?(.*)",           ApiUserAppHandeler),]

GLOBAL.routes.extend(routes)