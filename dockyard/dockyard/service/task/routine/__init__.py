from dockyard.var import GLOBAL
import pkgutil


class _Routine:
    KEY = None

    def __init__(self):
        GLOBAL.mq.subscribe(self.KEY, self)

    def callback(self, msg):
        try:
            ret = self._exec(**msg.attr)
            if ret:
                msg.received(self.KEY)
        except:
            pass

    def resume(self):
        raise NotImplemented

    def _exec(self, **kwargs):
        raise NotImplemented


def init():
    # init routine
    for loader, mod_name, is_pkg in pkgutil.walk_packages(__path__):
        mod = loader.find_module(mod_name).load_module(mod_name)
        mod.Routine()
