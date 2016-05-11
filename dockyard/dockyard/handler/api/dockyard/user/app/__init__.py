from dockyard.handler import BaseHandler
from dockyard.const.status import APIStatus
from dockyard.utils.wrapper import auth
from tornado.gen import coroutine

class ApiAppHandeler(BaseHandler):
    @coroutine
    def get(self, path, *args, **kwargs):
        if path == "list":  return self.get_apps()
        else:               return self.get_app()

    @coroutine
    def post(self, path, *args, **kwargs):
        pass

    @auth
    @coroutine
    def put(self, path, *args, **kwargs):
        pass

    @auth
    @coroutine
    def delete(self, path, *args, **kwargs):
        pass

    def get_app(self):
        pass

    def get_apps(self):
        pass