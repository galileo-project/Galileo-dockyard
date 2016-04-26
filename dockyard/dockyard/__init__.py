from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado import httpserver
from tornado.web import Application
from dockyard.route import routes
from dockyard.var import GLOBAL

def main(options):
    GLOBAL.mongo(options.mongo_host, options.mongo_port, options.database)
    app = Application(routes)
    app.listen(8080)
    IOLoop.instance().start()

if __name__ == "__main__":
    define("mongo_host",    "127.0.0.1",    str,    "mongodb host")
    define("mongo_port",    27017,          int,    "mongodb port")
    define("database",      "dockyard",     str,    "mongodb name")

    options.parse_command_line()
    main(options)