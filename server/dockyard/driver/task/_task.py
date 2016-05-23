import time
from dockyard.driver.task._model import Task
from dockyard.utils.driver import Driver


class TaskDriver(Task, Driver):
    def add(self, channel, msg, expire=-1):
        if expire != -1:
            expire = expire + time.time()

        self["channel"]   = channel
        self["msg"]       = msg
        self["receivers"] = []
        self["expire"]    = expire
        return self.succes(self)

    def gets_by_channel(self, channel, receiver):
        query = {"channel":   channel,
                 "receivers": self.q_nin([receiver])}
        query.update(self.q_or([{"expire": self.gt(time.time())},
                                {"expire": -1}]))

        self.find(query)
        if self.exists():
            return self.succes(self)
        else:
            return self.err(None)

    def received(self, receiver):
        self["receivers"].append(receiver)

    @property
    def expire(self):
        if self["expire"] == -1:
            return False
        elif self["expire"] < time.time():
            return True
        else:
            return False
