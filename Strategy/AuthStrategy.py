import json
import tornado.web
import base64
from tornado.web import Finish

def basic_auth(self):
	headers = self.request.headers
	auth = False
	if headers.get("Authorization")<>None: 
		print(headers["Authorization"])
		base64_str = base64.encodestring('wanglilong:123abc')
		print(base64_str)
		if headers["Authorization"]+'\n' == 'Basic '+base64_str:
			print('Basic '+base64_str)
			auth = True
	if auth == False:
		self.set_status(401)
		self.set_header('WWW-Authenticate', 'Basic realm="something"')
		raise Finish()

def digest_auth(self):
	headers = self.request.headers
	auth = True
	if headers.get("Authorization")<>None: 
		print(headers["Authorization"])
		#base64_str = base64.encodestring('wanglilong:123abc')
		#print(base64_str)
		if headers["Authorization"]+'\n' <> 'Basic '+base64_str:
			print('Basic '+base64_str)
			auth = False
	else:
		auth = False
	if auth == False:
		self.set_status(401)
		self.set_header('WWW-Authenticate', 'Digest realm="something",qop="auth",nonce="dcd98b7102dd2f0e8b11d0f600bfb0c093",opaque="5ccc069c403ebaf9f0171e9517f40e41"')
		raise Finish()
