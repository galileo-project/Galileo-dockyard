from dockyard.var import GLOBAL

routes = [("/auth/(.*)",                "",),
          (r"/api/user/github",         ""),
          (r"/api/app/?(.*)",           ""),]

GLOBAL.routes.extend(routes)