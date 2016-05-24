from dockyard.service.task._routines import _Routine


class __RoutineCheck(_Routine):
    PERIOD = 10

    @classmethod
    def _exec(cls, *args, **kwargs):
        pass


Routine = __RoutineCheck