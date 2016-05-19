from dockyard.service.routine._default import _Routine
from dockyard.var import GLOBAL

class __RoutineLog(_Routine):
    KEY = GLOBAL.CHAN_LOG

    def callback(self, msg):
        #do something
        msg.received(self.KEY)

    def resume(self):
        pass

Routine = __RoutineLog