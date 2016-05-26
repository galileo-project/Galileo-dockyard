from dockyard.service.interface import BaseHandler
from dockyard.const import APIStatus


class DefaultHandeler(BaseHandler):
    def get(self, *args, **kwargs):
        self.error(APIStatus["STAT_API_NOT_FOUND"])

    def post(self, *args, **kwargs):
        self.error(APIStatus["STAT_API_NOT_FOUND"])

    def delete(self, *args, **kwargs):
        self.error(APIStatus["STAT_API_NOT_FOUND"])

    def put(self, *args, **kwargs):
        self.error(APIStatus["STAT_API_NOT_FOUND"])
