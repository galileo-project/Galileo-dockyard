from dockyard.handler.api           import DefaultHandeler
from dockyard.handler.api.dockyard.auth import ApiAuthHandeler
from dockyard.handler.api.dockyard.user import ApiAppHandeler
from dockyard.handler.api.dockyard.user import ApiUserHandeler

routes = [(r"/api/user",        ApiUserHandeler),

          (r"/api/app/?(.*)",   ApiAppHandeler),

          (r"/auth/(.*)",       ApiAuthHandeler),
          (r"/(.*)",            DefaultHandeler),]