from tornado.web import RequestHandler
from tornado.gen import coroutine
from dockyard.const import APIStatus
from dockyard.model.user import User
from dockyard.model.sys.manager import Manager


class BaseHandler(RequestHandler):
    def initialize(self):
        RequestHandler.initialize(self)
        self._user      = None
        self._manager   = None

    def set_default_headers(self):
        origin = self.request.headers.get('Origin', '*')
        self.set_header('Access-Control-Allow-Origin',      origin)
        self.set_header('Access-Control-Allow-Methods',     'OPTIONS, HEAD, POST, DELETE, PUT, GET')
        self.set_header('Access-Control-Allow-Headers',     'Accept, Content-Type')

    @coroutine
    def prepare(self):
        self.finished = False
        self.data = {}

    def parse_arg(self, field, must):
        ret = self.get_argument(field, None)
        if ret is None and must:
            self.data_invalid()
        return ret

    def parse_arg_str(self, field, must, default = ""):
        ret = self.parse_arg(field, must)
        self.data[field] = default if ret is None else ret
        return ret

    def parse_arg_int(self, field, must, default = 0):
        ret = self.parse_arg(field, must)
        try:
            if ret is None:
                ret = default
            else:
                ret = int(ret)
        except:
            ret = default
        self.data[field] = ret
        return ret

    def parse_arg_bool(self, field, must, default = False):
        ret = self.parse_arg(field, must)
        if ret is None:
            ret = default
        else:
            ret = True if ret else False

        self.data[field] = ret
        return ret

    def data_invalid(self):
        self.error(APIStatus["STAT_API_DATA_INVALID"])

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
        print(self.data)
        if not self.finished:
            self.write(data)
            self.finished = True
            self.finish()

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

    @property
    def manager(self):
        if self._manager is None:
            manager_id_cookie = self.get_secure_cookie("manager")
            if manager_id_cookie:
                manager = Manager().get_by_id(manager_id_cookie)
                if manager:
                    self._manager = manager
                    return self._manager
            self._manager = Manager()

        return self._manager

    def set_user_cookie(self):
        self.set_secure_cookie("user", self.user.str_id)

    def del_user_cookie(self):
        self.set_secure_cookie("user", "", -1)

    def set_manager_cookie(self):
        self.set_secure_cookie("manager", self.user.str_id)

    def del_manager_cookie(self):
        self.set_secure_cookie("manager", "", -1)