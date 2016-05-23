from tornado.ioloop import IOLoop
from server.dockyard.const import ExpStatus


class __GlobalVar:
    __DATA                  = {}
    __INITIATED             = False

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

    # channel
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
    def task(self):
        name = "task"
        if not self.__DATA.get(name):
            from dockyard.service.task import TaskQueue
            self.__DATA[name] = TaskQueue()
        return self.__DATA[name]

    @classmethod
    def go(cls, func, *args, **kwargs):
        name = "go"
        if not cls.__DATA[name]:
            cls.__DATA[name] = IOLoop.instance()
        cls.__DATA[name].add_callback(func, *args, **kwargs)

    @property
    def routes(self):
        name = "routes"
        if not self.__DATA.get(name):
            self.__DATA[name] = []
        return self.__DATA[name]

    @property
    def logging(self):
        name = "logging"
        if not self.__DATA.get(name):
            from server.dockyard.driver.log import Log
            self.__DATA[name] = Log()
        return self.__DATA[name]

    def initialize(self):
        if not self.__INITIATED:
            self.__INITIATED = True
            from dockyard.service.task import init_routine
            init_routine()
            self.task.resume()


GLOBAL = __GlobalVar()
