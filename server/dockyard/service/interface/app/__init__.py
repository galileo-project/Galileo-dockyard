from dockyard.var import GLOBAL

from dockyard.service.interface.app._handler import ApiUserAppHandeler

routes = [(r"/api/app/?(.*)",           ApiUserAppHandeler),]

def init():
    GLOBAL.routes.extend(routes)