from dockyard.var import GLOBAL
from dockyard.utils.mongo import Mongo


class Manager(Mongo):
    """
    _id
    name
    password
    """
    def get_by_id(self, _id):
        return self.find_one({GLOBAL.MID: _id})
