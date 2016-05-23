from dockyard.var import GLOBAL

from server.dockyard.service.interface.app import ApiUserAppHandeler

routes = [(r"/api/app/?(.*)",           ApiUserAppHandeler),]

GLOBAL.routes.extend(routes)