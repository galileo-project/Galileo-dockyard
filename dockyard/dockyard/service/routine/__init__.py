import pkgutil

def init():
    for loader, mod_name, is_pkg in pkgutil.walk_packages(__path__):
        mod = loader.find_module(mod_name).load_module(mod_name)
        mod.Routine()