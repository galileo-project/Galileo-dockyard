from dockyard.var import GLOBAL

from server.dockyard.service.task import _Routine


class __RoutineBuild(_Routine):
    KEY = GLOBAL.CHAN_BUILD

    def _exec(self, arg=None):
        pass

    def resume(self):
        pass

Routine = __RoutineBuild