from dockyard.utils.mongo import Mongo


class User(Mongo):
    """
    _id
    name
    email
    password
    """
    def __init__(self):
        Mongo.__init__(self)
