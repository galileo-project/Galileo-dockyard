from dockyard.var import GLOBAL
from dockyard.service.interface.manager._handler import ApiManagerHandeler


routes = [
    (r'/api/manager', ApiManagerHandeler)
]


def init():
    GLOBAL.routes.extend(routes)