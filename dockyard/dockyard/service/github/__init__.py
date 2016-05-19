from dockyard.var import GLOBAL

routes = [(r"/api/public/github/(.*)",        "")]

GLOBAL.routes.extend(routes)