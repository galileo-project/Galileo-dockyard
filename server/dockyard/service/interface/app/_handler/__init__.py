from dockyard.utils.wrapper import auth
from tornado.gen import coroutine

from server.dockyard.utils.handler import BaseHandler


class ApiUserAppHandeler(BaseHandler):
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

    def get_status(self):
        pass