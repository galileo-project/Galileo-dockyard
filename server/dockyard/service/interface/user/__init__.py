from dockyard.var import GLOBAL
from dockyard.service.interface.user._handler import ApiUserHandeler
from dockyard.service.interface.user._handler.auth import ApiAuthHandeler

routes = [(r"/api/user",                ApiUserHandeler),
          (r"/auth/login",              ApiAuthHandeler),]

def init():
    GLOBAL.routes.extend(routes)