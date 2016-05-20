from dockyard.service.routine import _Routine
from dockyard.var import GLOBAL

class __RoutineBuild(_Routine):
    KEY = GLOBAL.CHAN_BUILD

    def _exec(self, arg=None):
        pass

    def resume(self):
        pass

Routine = __RoutineBuild