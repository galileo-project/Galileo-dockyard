from dockyard.handler.api                       import DefaultHandeler
from dockyard.handler.api.dockyard.auth         import ApiAuthHandeler
from dockyard.handler.api.dockyard.user.app     import ApiUserAppHandeler
from dockyard.handler.api.dockyard.user         import ApiUserHandeler
from dockyard.handler.api.dockyard.user.github  import ApiUserGitHubHandeler

routes = [(r"/api/user",        ApiUserHandeler),
          (r"/api/user/github", ApiUserGitHubHandeler),
          (r"/api/app/?(.*)",   ApiUserAppHandeler),

          (r"/auth/(.*)",       ApiAuthHandeler),
          (r"/(.*)",            DefaultHandeler),]