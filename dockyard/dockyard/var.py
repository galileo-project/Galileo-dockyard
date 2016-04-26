from pymongo.mongo_client import MongoClient
from dockyard.const.status import ExpStatus

class Global:
    def __init__(self):
        self.__data = {}

    def mongo(self, host = None, port = None, database = None):
        _name = "mongo"
        if not self.__data.get(_name):
            if not host or not port or not database:
                raise Exception(ExpStatus["STAT_EXP_INIT_MONGO"])
            client = MongoClient(host, port)
            self.__data[_name] = client[database]
        return self.__data[_name]


GLOBAL = Global()