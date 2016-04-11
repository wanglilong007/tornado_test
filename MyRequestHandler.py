import json
from AuthStrategy import basic_auth
from JsonStrategy import json_handle
import tornado.web

class MyRequestHandler(tornado.web.RequestHandler):

	def initialize(self):
		self.auth_handler = basic_auth 
		self.json_handler = json_handle

	def prepare(self):
		self.auth_handler(self)
		self.json_handler(self)
