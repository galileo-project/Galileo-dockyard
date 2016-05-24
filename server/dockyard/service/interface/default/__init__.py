from dockyard.var import GLOBAL
from dockyard.service.interface.default._handler import DefaultHandeler

routes = [(r"/(.*)",                DefaultHandeler)]

def init():
    GLOBAL.routes.extend(routes)