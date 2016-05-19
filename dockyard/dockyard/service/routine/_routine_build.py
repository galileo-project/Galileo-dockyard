from dockyard.service.routine import _Routine
from dockyard.var import GLOBAL

class __RoutineBuild(_Routine):
    KEY = GLOBAL.CHAN_BUILD

    def _exec(self, msg):
        pass

    def resume(self):
        pass

Routine = __RoutineBuild