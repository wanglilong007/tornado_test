from tornado.web import Finish 
import tornado.web
import MyRequestHandler
import json

class NodeHandler(MyRequestHandler.MyRequestHandler):
	def get(self):
		node = {"name":"esurvey1","os":"windows","ip":"10.68.51.120"}
		self.set_header('Content-Type', 'application/json')
		self.write(json.dumps(node))

	def post(self):
		body = self.json_body
		headers = self.request.headers
		self.set_header('Content-Type', 'application/json')
		self.write(json.dumps(body))

	def put(self):
		self.write("Hello, put node")

	def delete(self):
		self.write("Hello, delete node")

class osHandler(MyRequestHandler.MyRequestHandler):

	def prepare(self):
		self.auth_handler = None
	def get(self):
		os = {"total":3,"support_os":["windows","ubuntu","centos"],"version":"F"}
		self.set_header('Content-Type', 'application/json')
		self.write(json.dumps(os))
