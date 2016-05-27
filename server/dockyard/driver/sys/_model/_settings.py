from dockyard.utils.mongo import Mongo
from dockyard.var import GLOBAL

class System(Mongo):
    """
    _id
    github_client_id
    github_client_secret
    github_redirect_uri
    """
    KEY = "SETTINGS"