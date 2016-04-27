from tornado.web import RequestHandler
from tornado.gen import coroutine
from dockyard.const import APIStatus
from dockyard.model.user import User

class BaseHandler(RequestHandler):
    def initialize(self):
        RequestHandler.initialize(self)
        self._user = None

    @coroutine
    def prepare(self):
        self.data = {}


    def parse_arg(self, field, must):
        ret = self.get_argument(field, None)
        if ret is None and must:
            self.data_invalid()
        return ret

    def parse_arg_str(self, field, default = "", must = True):
        ret = self.parse_arg(field, must)
        self.data[field] = default if ret is None else ret
        return ret

    def parse_arg_int(self, field, default = 0, must = True):
        ret = self.parse_arg(field, must)
        try:
            if ret is None:
                ret = 0
            else:
                ret = int(ret)
        except:
            ret = 0
        self.data[field] = ret
        return ret

    def parse_arg_bool(self, field, default = False, must = True):
        ret = self.parse_arg(field, must)
        if ret is None:
            ret = default
        else:
            ret = True if ret else False

        self.data[field] = ret
        return ret

    def data_invalid(self):
        self.error(APIStatus["STAT_API_DATA_INVALID"])
        self.finish()

    def error(self, status = None):
        if not status:
            status = APIStatus["STAT_API_UNKNOWN_ERROR"]
        self.export(None, status)

    def success(self, data = None):
        status = APIStatus["STAT_API_SUCCESS"]
        self.export(data, status)

    def export(self, msg, status):
        data = {"code":     status[0],
                "msg":      msg,
                "error":    status[1]}
        self.raw_export(data)

    def raw_export(self, data):
        self.write(data)

    @property
    def user(self):
        if self._user is None:
            user_id_cookie = self.get_secure_cookie("user")
            if user_id_cookie:
                user = User().get_by_id(user_id_cookie)
                if user:
                    self._user = user
                    return self._user
            self._user = User()

        return self._user