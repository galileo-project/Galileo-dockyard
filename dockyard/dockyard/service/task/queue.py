from dockyard.service.task._model import MsgModel
from dockyard.var import GLOBAL
from tornado.ioloop import IOLoop


class TaskQueue:
    def __init__(self):
        self.__subscriber = {}

    def send(self, channel, expire=-1, **kwargs):
        task = MsgModel().add(channel, kwargs, expire)
        callback = self.__subscriber[channel].callback
        IOLoop.instance().add_callback(callback, task)

    def broadcast(self, expire=-1, **kwargs):
        task = MsgModel().add(GLOBAL.CHAN_GLOBAL, kwargs, expire)
        self.__broadcast(task)

    def subscribe(self, channel, subscriber):
        if channel not in self.__subscriber:
            self.__subscriber[channel] = subscriber

    def __broadcast(self, task):
        for subscriber in self.__subscriber.values():
            IOLoop.instance().add_callback(subscriber.callback, task)
