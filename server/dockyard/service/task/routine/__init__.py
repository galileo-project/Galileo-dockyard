import pkgutil
from server.dockyard.var import GLOBAL


class _Routine:
    KEY = None

    def __init__(self):
        GLOBAL.mq.subscribe(self)

    def callback(self, task):
        try:
            ret = self._exec(**task.attr["msg"])
            if ret:
                task.received(self.KEY)
        except:
            pass

    def _exec(self, **kwargs):
        raise NotImplemented


def init():
    # init routine
    for loader, mod_name, is_pkg in pkgutil.walk_packages(__path__):
        mod = loader.find_module(mod_name).load_module(mod_name)
        mod.Routine()
