from dockyard.var import GLOBAL
from dockyard.service.task.routine import _Routine


class __RoutineBuild(_Routine):
    KEY = GLOBAL.CHAN_BUILD

    def _exec(self, arg=None):
        pass

Routine = __RoutineBuild