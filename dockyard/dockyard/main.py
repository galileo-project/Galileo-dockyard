from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado import httpserver
from tornado.web import Application
from dockyard.var import GLOBAL
from dockyard.utils import gen_random
from dockyard.service.task import init_routine

def main(options):
    GLOBAL.mongo(options.mongo_host, options.mongo_port, options.database)

    settings = {"login_url"    : "/auth/login",
                "debug"        : options.debug,
                "cookie_secret": "233" if options.debug else gen_random(16)}
    app = Application(GLOBAL.routes, **settings)
    server = httpserver.HTTPServer(app)
    server.bind(options.port, options.address)
    server.start(options.process)
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