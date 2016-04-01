import tornado.ioloop
import tornado.web
import nodes
import version
#from nodes import NodeHandler

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/version",version.VersionHandler),
    (r"/nodes", nodes.NodeHandler),
    (r"/nodes/os", nodes.osHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
