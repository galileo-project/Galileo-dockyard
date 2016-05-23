from dockyard.utils.mongo import Mongo


class User(Mongo):
    def __init__(self):
        Mongo.__init__(self)
