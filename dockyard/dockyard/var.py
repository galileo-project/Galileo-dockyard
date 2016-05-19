from dockyard.const.status import ExpStatus

class __GlobalVar:
    __DATA                  = {}
    MID                     = "_id"
    MDELETE                 = "__deleted__"
    MCREATE                 = "__create__"
    MUPDATE                 = "__update__"

    LOG_WARN                = "warn"
    LOG_FATAL               = "fatal"
    LOG_SUCCESS             = "success"
    LOG_ERROR               = "error"
    LOG_INFO                = "info"

    SYS_ORIGIN              = "system"

    LOG_ERROR_LEVEL         = "_error",
    LOG_FATAL_LEVEL         = "_fatal",
    LOG_SUCCESS_LEVEL       = "_success",
    LOG_WARN_LEVEL          = "_warn",
    LOG_PUTS_LEVEL          = "_put"

    GITHUB_OAUTH_REDIRECT   = ""

    #channel
    CHAN_GLOBAL             = "global_chan"
    CHAN_BUILD              = "build_chan"
    CHAN_LOG                = "log_chan"

    def mongo(self, host=None, port=None, database=None):
        name = "mongo"
        if not self.__DATA.get(name):
            from pymongo.mongo_client import MongoClient
            if not host or not port or not database:
                raise Exception(ExpStatus["STAT_EXP_INIT_MONGO"])
            client = MongoClient(host, port)
            self.__DATA[name] = client[database]
        return self.__DATA[name]

    @property
    def mq(self):
        name = "mq"
        if not self.__DATA.get(name):
            from dockyard.service.queue import taskQueue
            self.__DATA[name] = taskQueue()
        return self.__DATA[name]

    @property
    def routes(self):
        name = "routes"
        if not self.__DATA.get(name):
            self.__DATA[name] = []
        return self.__DATA[name]

    def logging(self):
        name = "logging"
        if not self.__DATA.get(name):
            from dockyard.service.log import logging
            self.__DATA[name] = logging()
        return self.__DATA[name]


GLOBAL = __GlobalVar()