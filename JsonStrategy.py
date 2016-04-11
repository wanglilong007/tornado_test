import json
import tornado.web

def json_handle(self):
	print('handle json\n')
	headers = self.request.headers
	if headers.get("Content-Type")<>None and headers["Content-Type"].startswith("application/json"):
		self.json_body = json.loads(self.request.body)
	else:
		self.json_body = None
