from dockyard.const.status import ExpStatus

class __GlobalVar:
    MID                     = "_id"
    MDELETE                 = "__deleted__"
    MCREATE                 = "__create__"
    MUPDATE                 = "__update__"

    LOG_WARN                = "warn"
    LOG_FATAL               = "fatal"
    LOG_SUCCESS             = "success"
    LOG_ERROR               = "error"
    LOG_PUTS                = "put"

    SYS_ORIGIN              = "system"

    LOG_ERROR_LEVEL         = "_error",
    LOG_FATAL_LEVEL         = "_fatal",
    LOG_SUCCESS_LEVEL       = "_success",
    LOG_WARN_LEVEL          = "_warn",
    LOG_PUTS_LEVEL          = "_put"

    GITHUB_OAUTH_REDIRECT   = ""

    def __init__(self):
        self.__data = {}

    def mongo(self, host = None, port = None, database = None):
        _name = "mongo"
        if not self.__data.get(_name):
            from pymongo.mongo_client import MongoClient
            if not host or not port or not database:
                raise Exception(ExpStatus["STAT_EXP_INIT_MONGO"])
            client = MongoClient(host, port)
            self.__data[_name] = client[database]
        return self.__data[_name]

    @property
    def log(self):
        _name = "log"
        if not self.__data.get(_name):
            from dockyard.model.logs import Log
            self.__data[_name] = Log()
        return self.__data[_name]

GLOBAL = __GlobalVar()