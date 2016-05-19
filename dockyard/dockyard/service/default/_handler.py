from dockyard.utils.handler import BaseHandler

class DefaultHandeler(BaseHandler):
    def get(self, *args, **kwargs):
        self.success()

    def post(self, *args, **kwargs):
        self.success()

    def delete(self, *args, **kwargs):
        self.success()

    def put(self, *args, **kwargs):
        self.success()
