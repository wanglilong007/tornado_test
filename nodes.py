from tornado.web import Finish 
import BasicAuthRequest
import DigestAuthRequest
import json
import JsonRequest
import subprocess

class NodeHandler(JsonRequest.JsonRequestHandler):
	def get(self):
		self.write("Hello, get node")
		subprocess.call("ls -l",shell=True)
	def post(self):
		body = self.json_body
		headers = self.request.headers

		node_name = body["name"]
		node_os = body["os"]
		node_ip = body["host"]
		node_role = body["role"]
		node_user = body["user"]
		node_pass = body["password"]
		self.write("Hello, post node")
		self.write(node_name)
		self.write(node_os)
		self.write(node_ip)
		self.write(node_user)
		self.write(node_pass)

	def put(self):
		self.write("Hello, put node")
	def delete(self):
		self.write("Hello, delete node")

class osHandler(DigestAuthRequest.DigestAuthRequestHandler):
	def get(self):
		self.write('send support os')
		os = {"support_os":["windows","ubuntu","centos"]}
		self.write(json.dumps(os))
