from dockyard.service.routine import _Routine
from dockyard.var import GLOBAL

class __RoutineLog(_Routine):
    KEY = GLOBAL.CHAN_LOG

    def _exec(self, msg):
        pass

    def resume(self):
        pass

Routine = __RoutineLog