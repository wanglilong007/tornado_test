import tornado.web

class NodeHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, get node")

    def post(self):
        self.write("Hello, post node")
    def put(self):
        self.write("Hello, put node")
    def delete(self):
        self.write("Hello, delete node")

