from dockyard.service.routine import _Routine
from dockyard.var import GLOBAL

class __RoutineLog(_Routine):
    KEY = GLOBAL.CHAN_LOG

    def _exec(self, task):
        msg = task["msg"]

    def resume(self):
        pass

Routine = __RoutineLog