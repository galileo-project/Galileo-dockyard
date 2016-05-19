from dockyard.service.routine._default import _Routine
from dockyard.var import GLOBAL

class __RoutineBuild(_Routine):
    KEY = GLOBAL.CHAN_BUILD

    def callback(self, msg):
        #do something
        msg.received(self.KEY)

    def resume(self):
        pass

Routine = __RoutineBuild