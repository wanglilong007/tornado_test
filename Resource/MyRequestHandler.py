import json
import sys
sys.path.append("..")
import Strategy
#from AuthStrategy import basic_auth
#from JsonStrategy import json_handle
import tornado.web

class MyRequestHandler(tornado.web.RequestHandler):

	def initialize(self):
		self.auth_handler = Strategy.AuthStrategy.basic_auth 
		self.json_handler = Strategy.JsonStrategy.json_handle

	def prepare(self):
		self.auth_handler(self)
		self.json_handler(self)
