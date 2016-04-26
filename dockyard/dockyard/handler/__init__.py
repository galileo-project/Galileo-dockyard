from tornado.web import RequestHandler
from dockyard.const import APIStatus

class BaseHandler(RequestHandler):
    def initialize(self):
        pass

    def error(self, status):
        self.export(None, status)

    def success(self, data):
        status = APIStatus["STAT_API_SUCCESS"]
        self.export(data, status)

    def export(self, msg, status):
        data = {"code":     status[0],
                "msg":      msg,
                "error":    status[1]}
        self.raw_export(data)

    def raw_export(self, data):
        self.write(data)