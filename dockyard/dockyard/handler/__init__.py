from tornado.web import RequestHandler

class BaseHandler(RequestHandler):
    def initialize(self):
        pass
    