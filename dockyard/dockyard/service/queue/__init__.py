from dockyard.service.queue._model import MsgModel
from dockyard.var import GLOBAL
from tornado.ioloop import IOLoop

class MsgQueue:
    def __init__(self):
        self.__subscriber = {}

    def send(self, channel, msg, expire=-1, *args, **kwargs):
        msg = MsgModel().add(channel, msg, expire)
        callback = self.__subscriber[channel].callback
        IOLoop.instance().add_callback(callback, msg)

    def broadcast(self, msg, expire=-1, *args, **kwargs):
        msg = MsgModel().add(GLOBAL.CHAN_GLOBAL, msg, expire)
        self.__broadcast(msg)

    def subscribe(self, channel, subscriber):
        if not channel in self.__subscriber:
            self.__subscriber[channel] = subscriber

    def __broadcast(self, msg):
        for subscriber in self.__subscriber.values():
            IOLoop.instance().add_callback(subscriber.callback, msg)
