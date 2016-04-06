import json
from AuthDecorator import test
from AuthDecorator import basic_auth
from JsonDecorator import json_handle
import tornado.web

class VersionHandler(tornado.web.RequestHandler):
#	@basic_auth
#	@json_handle
	def get(self):
		version = {"date": "", "commit": "", "version": "3.1.0", "build": "85"}
		self.set_header('Content-Type', 'application/json')
		self.write(json.dumps(version))
