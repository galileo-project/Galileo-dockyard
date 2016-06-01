from dockyard.driver.manager import Manager
from dockyard.driver.user import User
from tornado.gen import coroutine
from tornado.web import RequestHandler
from dockyard.const import APIStatus
from dockyard.var import GLOBAL
import pkgutil


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

    def return_driver(self, m):
        err, msg = m
        if err:
            return self.error(msg)
        else:
            return self.success(msg)

    def error(self, status=None):
        if not status:
            status = APIStatus["STAT_API_UNKNOWN_ERROR"]
        self.export(None, status)

    def success(self, data=None):
        if isinstance(data, tuple):
            status = data
            data   = None
        else:
            status = APIStatus["STAT_API_SUCCESS"]
        self.export(data, status)

    def export(self, msg, status):
        data = {"code":     status[0],
                "data":     msg,
                "info":     status[1]}
        self.raw_export(data)

    def raw_export(self, data):
        if not self.finished:
            self.write(data)
            self.finished = True
            self.finish()

    @property
    def user(self):
        if self._user is None:
            user_id_cookie = self.get_secure_cookie("user")
            print(user_id_cookie)
            if user_id_cookie:
                self._user = User().get_by_id(user_id_cookie)
            else:
                self._user = User()
        return self._user

    @property
    def manager(self):
        if self._manager is None:
            manager_id_cookie = self.get_secure_cookie("manager")
            if manager_id_cookie:
                self._manager = Manager().get_by_id(manager_id_cookie)
            else:
                self._manager = Manager()
        return self._manager

    def set_user_cookie(self):
        print(self.user.str_id)
        self.set_secure_cookie("user", self.user.str_id)

    def del_user_cookie(self):
        self.set_secure_cookie("user", "", -1)

    def set_manager_cookie(self):
        self.set_secure_cookie("manager", self.manager.str_id)

    def del_manager_cookie(self):
        self.set_secure_cookie("manager", "", -1)


def init_interface():
    # init routes
    for loader, mod_name, is_pkg in pkgutil.walk_packages(__path__):
        mod = loader.find_module(mod_name).load_module(mod_name)
        try:
            mod.init()
        except AttributeError:
            pass

    from dockyard.service.interface.default import routes as default_routes
    GLOBAL.routes.extend(default_routes)