from dockyard.utils.mongo import Mongo
from dockyard.var import GLOBAL


class Manager(Mongo):
    """
    _id
    name
    password
    """
    def get_by_id(self, _id):
        return self.find_one({GLOBAL.MID: _id})
