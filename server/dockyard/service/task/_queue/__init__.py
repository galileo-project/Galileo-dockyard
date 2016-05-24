import pkgutil
from dockyard.var import GLOBAL


class _Queue:
    KEY = None

    def subscribe(self):
        GLOBAL.tq.subscribe(self)

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
    # init queue
    for loader, mod_name, is_pkg in pkgutil.walk_packages(__path__):
        mod = loader.find_module(mod_name).load_module(mod_name)
        mod.Queue().subscribe()
