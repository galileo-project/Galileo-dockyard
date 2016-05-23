import pkgutil
from tornado.ioloop import PeriodicCallback


class _Routine:
    PERIOD = None

    def callback(self):
        self._exec()

    def _exec(self, *args, **kwargs):
        raise NotImplemented


def init():
    # init routines
    for loader, mod_name, is_pkg in pkgutil.walk_packages(__path__):
        mod = loader.find_module(mod_name).load_module(mod_name)
        if mod.PERIOD is not None:
            PeriodicCallback(mod.callback, mod.PERIOD).start()
