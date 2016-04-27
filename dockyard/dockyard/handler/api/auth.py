from dockyard.handler import BaseHandler

class ApiAuthHandeler(BaseHandler):
    def get(self, *args, **kwargs):
        self.success(self.user)