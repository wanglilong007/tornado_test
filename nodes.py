from tornado.web import Finish 
import tornado.web
import json
from AuthDecorator import basic_auth
from JsonDecorator import json_handle

class NodeHandler(tornado.web.RequestHandler):
	@basic_auth
	@json_handle
	def get(self):
		node = {"name":"esurvey1","os":"windows","ip":"10.68.51.120"}
		self.write(json.dumps(node))

	@basic_auth
	@json_handle
	def post(self):
		body = self.json_body
		headers = self.request.headers
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
		os = {"total":3,"support_os":["windows","ubuntu","centos"],"version":"F"}
		self.set_header('Content-Type', 'application/json')
		self.write(json.dumps(os))
