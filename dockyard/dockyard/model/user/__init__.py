from dockyard.utils.mongo import Mongo

class User(Mongo):
    def get_by_id(self, _id):
        return self.find_one({Mongo.MID : _id})