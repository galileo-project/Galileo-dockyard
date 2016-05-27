from dockyard.var import GLOBAL
from dockyard.service.interface.manager._handler import ApiManagerHandeler
from dockyard.service.interface.manager._handler._auth import ApiAuthHandeler
from dockyard.service.interface.manager._handler._users import ApiUsersHandeler


routes = [
    (r'/api/manager/settings',      ApiManagerHandeler),
    (r'/api/manager/user',          ApiUsersHandeler),
    (r'/api/manager/auth/(.*)',     ApiAuthHandeler,)
]


def init():
    GLOBAL.routes.extend(routes)