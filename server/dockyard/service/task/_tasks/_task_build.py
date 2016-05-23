from dockyard.var import GLOBAL
from dockyard.service.task._tasks import _Task


class __TaskBuild(_Task):
    KEY = GLOBAL.CHAN_BUILD

    def _exec(self, arg=None):
        pass

Task = __TaskBuild