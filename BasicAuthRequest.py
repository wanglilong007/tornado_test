import json
import tornado.web
import base64
from tornado.web import Finish

class AuthRequestHandler(tornado.web.RequestHandler):
	def prepare(self):
		headers = self.request.headers
		auth = True
		if headers.get("Authorization")<>None: 
			print(headers["Authorization"])
			base64_str = base64.encodestring('wanglilong:123abc')
			print(base64_str)
			if headers["Authorization"]+'\n' <> 'Basic '+base64_str:
				print('Basic '+base64_str)
				auth = False
		else:
			auth = False
		if auth == False:
			self.set_status(401)
			self.set_header('WWW-Authenticate', 'Basic realm="something"')
			raise Finish()
