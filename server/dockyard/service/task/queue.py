from dockyard.var import GLOBAL
from tornado.ioloop import IOLoop
from dockyard.driver.task import Task


class TaskQueue:
    def __init__(self):
        self.__subscriber = {}

    def send(self, channel, expire=-1, **kwargs):
        err, task = Task().add(channel, kwargs, expire)
        callback = self.__subscriber[channel].callback
        IOLoop.instance().add_callback(callback, task)

    def broadcast(self, expire=-1, **kwargs):
        err, task = Task().add(GLOBAL.CHAN_GLOBAL, kwargs, expire)
        self.__broadcast(task)

    def subscribe(self, subscriber):
        if subscriber.KEY:
            if subscriber.KEY not in self.__subscriber:
                self.__subscriber[subscriber.KEY] = subscriber

    def resume(self):
        pass

    def __broadcast(self, task):
        for subscriber in self.__subscriber.values():
            IOLoop.instance().add_callback(subscriber.callback, task)
