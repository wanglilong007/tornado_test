import json
import tornado.web

class JsonRequestHandler(tornado.web.RequestHandler):
	def prepare(self):
		headers = self.request.headers
		if headers.get("Content-Type")<>None and headers["Content-Type"].startswith("application/json"):
			self.json_body = json.loads(self.request.body)
		else:
			self.json_body = None
