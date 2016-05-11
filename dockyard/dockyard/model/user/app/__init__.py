from dockyard.utils.mongo import Mongo
from dockyard.var import GLOBAL


class UserApp(Mongo):
    def __init__(self, user=None):
        Mongo.__init__(self)
        if user:
            self.set_query({"user": user[GLOBAL.MID]})

    def get_by_id(self, _id):
        return self.find_one({GLOBAL.MID: _id})
