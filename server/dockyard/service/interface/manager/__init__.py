from dockyard.var import GLOBAL
from dockyard.service.interface.manager._handler._auth import ApiAuthHandeler
from dockyard.service.interface.manager._handler._users import ApiUsersHandeler
from dockyard.service.interface.manager._handler._sys import ApiSysHandeler


routes = [
    (r'/api/manager/user',          ApiUsersHandeler),
    (r'/api/manager/sys/(.*)',      ApiSysHandeler),
    (r'/api/manager/auth/(.*)',     ApiAuthHandeler,)
]


def init():
    GLOBAL.routes.extend(routes)