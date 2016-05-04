from dockyard.handler.api           import DefaultHandeler
from dockyard.handler.api.user      import ApiUserHandeler
from dockyard.handler.api.user.app  import ApiAppHandeler
from dockyard.handler.api.auth      import ApiAuthHandeler

routes = [(r"/api/user",        ApiUserHandeler),

          (r"/api/app/?(.*)",   ApiAppHandeler),

          (r"/auth/(.*)",       ApiAuthHandeler),
          (r"/(.*)",            DefaultHandeler),]