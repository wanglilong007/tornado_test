import tornado.web
import JsonRequest

class NodeHandler(JsonRequest.JsonRequestHandler):
	def get(self):
		self.write("Hello, get node")
	def post(self):
		body = self.json_body
		headers = self.request.headers
		self.write("Hello, post node")
		print(type(headers))
		print(type(body))
		print(body["name"])
		print(body["age"])

	def put(self):
		self.write("Hello, put node")
	def delete(self):
		self.write("Hello, delete node")

class osHandler(JsonRequest.JsonRequestHandler):
	def get(self):
		self.write('send support os')
		print(self.get_query_arguments('name'))
		print(self.get_query_arguments('age'))
		
