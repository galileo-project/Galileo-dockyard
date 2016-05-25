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

    def __init__(self):
        Mongo.__init__(self)
        self.find_one({GLOBAL.MKEY: self.KEY})
        self[GLOBAL.MKEY] = self.KEY