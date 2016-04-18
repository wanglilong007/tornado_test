import tornado.wsgi
import sae

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world! - Tornado")

app = tornado.wsgi.WSGIApplication([
    (r"/", MainHandler),
    (r"/users", Resource.users.UserHandler),
    (r"/nodes", Resource.nodes.NodeHandler),
    (r"/nodes/os", Resource.nodes.osHandler),
    (r"/version",Resource.version.VersionHandler),
])

application = sae.create_wsgi_app(app)