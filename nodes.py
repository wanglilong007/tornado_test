from tornado.web import Finish 
import tornado.web
import json
from AuthDecorator import basic_auth
from JsonDecorator import json_handle

class NodeHandler(tornado.web.RequestHandler):
	@basic_auth
	@json_handle
	def get(self):
		self.write("Hello, get node")

	@basic_auth
	@json_handle
	def post(self):
		body = self.json_body
		headers = self.request.headers
		'''
		node_name = body["name"]
		node_os = body["os"]
		node_ip = body["host"]
		node_role = body["role"]
		node_user = body["user"]
		node_pass = body["password"]
		'''
		self.set_header('Content-Type', 'application/json')
		self.write(json.dumps(body))

	@basic_auth
	@json_handle
	def put(self):
		self.write("Hello, put node")

	@basic_auth
	@json_handle
	def delete(self):
		self.write("Hello, delete node")

class osHandler(tornado.web.RequestHandler):

	@basic_auth
	@json_handle
	def get(self):
		#self.write('send support os')
		os = {"total":3,"support_os":["windows","ubuntu","centos"],"version":"F"}
		self.set_header('Content-Type', 'application/json')
		self.write(json.dumps(os))
