from dockyard.var import GLOBAL

routes = [(r"/api/user",                "",),
          (r"/api/user/github",         ""),
          (r"/api/app/?(.*)",           ""),]

GLOBAL.routes.extend(routes)