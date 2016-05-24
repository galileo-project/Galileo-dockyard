import pkgutil
from tornado.ioloop import PeriodicCallback


class _Routine:
    PERIOD = None

    @classmethod
    def callback(cls):
        cls._exec()

    @classmethod
    def _exec(cls, *args, **kwargs):
        raise NotImplemented


def init():
    # init routines
    for loader, mod_name, is_pkg in pkgutil.walk_packages(__path__):
        mod = loader.find_module(mod_name).load_module(mod_name).Routine
        if mod.PERIOD is not None:
            PeriodicCallback(mod.callback, mod.PERIOD).start()
