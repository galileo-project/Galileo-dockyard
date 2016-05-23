from dockyard.utils import gen_random
from dockyard.var import GLOBAL
from tornado import httpserver
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application

from server.dockyard.service.task import init_routine


def main(opt):
    GLOBAL.mongo(opt.mongo_host, opt.mongo_port, opt.database)

    settings = {"login_url"    : "/auth/login",
                "debug"        : opt.debug,
                "cookie_secret": "233" if opt.debug else gen_random(16)}
    app = Application(GLOBAL.routes, **settings)
    server = httpserver.HTTPServer(app)
    server.bind(opt.port, opt.address)
    server.start(opt.process)
    init_routine()

    IOLoop.instance().start()

if __name__ == "__main__":
    define("address",       "0.0.0.0",          str,    "dockyard address")
    define("port",          8080,               int,    "dockyard port")
    define("process",       1,                  int,    "process")
    define("debug",         True,               bool,   "debug")

    define("mongo_host",    "127.0.0.1",        str,    "mongodb host")
    define("mongo_port",    27017,              int,    "mongodb port")
    define("database",      "dockyard",         str,    "mongodb name")

    options.parse_command_line()
    main(options)
