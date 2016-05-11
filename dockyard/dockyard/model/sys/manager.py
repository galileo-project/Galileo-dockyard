from dockyard.utils.mongo import Mongo
from dockyard.var import GLOBAL


class Manager(Mongo):
    def get_by_id(self, _id):
        return self.find_one({GLOBAL.MID: _id})
