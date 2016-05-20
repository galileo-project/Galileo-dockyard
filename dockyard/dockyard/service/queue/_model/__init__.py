from dockyard.utils.mongo import Mongo
import time

class MsgModel(Mongo):
    """
        channel
        msg
        receivers
        expire
    """
    def add(self, channel, msg, expire=-1):
        if expire != -1:
            expire = expire + time.time()

        self["channel"]   = channel
        self["msg"]       = msg
        self["receivers"] = []
        self["expire"]    = expire
        return self

    def gets_by_channel(self, channel, receiver):
        self.find_one({"channel":   channel,
                       "receivers": self.q_nin([receiver])})

        if self.exists():
            return self
        else:
            return None

    def received(self, receiver):
        self["receivers"].append(receiver)

    @property
    def expire(self):
        if self["expire"] < time.time():
            return False
        else:
            return True
