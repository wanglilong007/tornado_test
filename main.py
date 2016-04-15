import tornado.ioloop
import tornado.web
import Resource
#from nodes import NodeHandler

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/users", Resource.users.UserHandler),
    (r"/nodes", Resource.nodes.NodeHandler),
    (r"/nodes/os", Resource.nodes.osHandler),
    (r"/version",Resource.version.VersionHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
