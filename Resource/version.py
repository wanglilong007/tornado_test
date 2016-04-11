import json
import tornado.web

class VersionHandler(tornado.web.RequestHandler):

	def get(self):
		version = {"date":"","commit": "", "version": "3.1.0", "build": 85}
		self.set_header('Content-Type', 'application/json')
		self.write(json.dumps(version))
