from dockyard.var import GLOBAL
from dockyard.service.task._queue import _Queue


class __QueueBuild(_Queue):
    KEY = GLOBAL.CHAN_BUILD

    def _exec(self, arg=None):
        pass

Queue = __QueueBuild
