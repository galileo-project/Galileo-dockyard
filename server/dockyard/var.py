import threading
from tornado.ioloop import IOLoop
from dockyard.const import ExpStatus
import logging


class __GlobalVar:
    __INSTANCE              = None
    __DATA                  = {}
    __INITIATED             = False
    __LOCK                  = threading.Lock()

    MID                     = "__id__"
    MDELETE                 = "__deleted__"
    MCREATE                 = "__create__"
    MUPDATE                 = "__update__"
    MKEY                    = "__key__"

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

    def __new_instance(self, name, cls, *args, **kwargs):
        if not self.__DATA.get(name):
            self.__DATA[name] = cls(*args, **kwargs)
        return self.__DATA[name]

    def mongo(self, host=None, port=None, database=None):
        name = "mongo"
        if not self.__DATA.get(name):
            from pymongo.mongo_client import MongoClient
            if not host or not port or not database:
                raise Exception(ExpStatus["STAT_EXP_INIT_MONGO"])
            self.__new_instance(name, MongoClient, host, port)
        return self.__DATA[name][database]

    @property
    def tq(self):
        # return singleton instance of task queue
        name = "tq"
        if not self.__DATA.get(name):
            from dockyard.service.task import TaskQueue
            self.__new_instance(name, TaskQueue)
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
            self.__new_instance(name, Log)
        return self.__DATA[name]

    @staticmethod
    def puts(*args, **kwargs):
        logging.info(*args, **kwargs)

    def initialize(self):
        if not self.__INITIATED:
            with self.__LOCK:
                if not self.__INITIATED:
                    self.__INITIATED = True
                    from dockyard.service.task import init_queue
                    from dockyard.service.task import init_routine
                    from dockyard.service.interface import init_interface

                    self.puts("Init task queue ...")
                    init_queue()
                    self.puts("Init routine ...")
                    init_routine()
                    self.puts("Init interface ...")
                    init_interface()
                    self.puts("Resume task queue ...")
                    self.tq.resume()

    @classmethod
    def instance(cls, *args, **kwargs):
        if cls.__INSTANCE is None:
            with cls.__LOCK:
                if cls.__INSTANCE is None:
                    cls.__INSTANCE = cls(*args, **kwargs)
        return cls.__INSTANCE


GLOBAL = __GlobalVar.instance()
