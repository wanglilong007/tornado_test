from tornado.web import Finish 
import tornado.web
import sys
sys.path.append("..")
from MyRequestHandler import *
import json
import peewee
from DBmodel.UserModel import User
import datetime

class UserHandler(MyRequestHandler):
	def get(self):
		users_li = []
		user_o = {}
		users = User.select()
		for user in users:
			#print user.name
			#user_o["name"] = user.name
			#user_o["sex"] = user.sex
			#print user_o
			users_li.append({"name":user.name,"sex":user.sex})
			#print users_li

		self.set_header('Content-Type', 'application/json')
		self.write(json.dumps(users_li))

	def post(self):
		body = self.json_body
		headers = self.request.headers
		user_name = body['name']
		user_pwd = body['password']
		user_sex = body['sex']
		user_addr = body['address']
		user_birthday = body['birthday']
		user_statement = body['statement']

		print(user_name,user_pwd,user_sex,user_birthday,user_statement)
		if user_name=='' or user_pwd=='':
			self.set_status(400)
			raise Finish()

		new_user = User.create(name=user_name,password=user_pwd,sex=user_sex,address=user_addr,birthday=user_birthday,statement=user_statement)
		#new_user.sex = user_sex
		#new_user.birthday = user_birthday
		#new_user.statement = user_statement

		new_user.save()
		self.set_header('Content-Type', 'application/json')
		self.write(json.dumps(body))

	def put(self):
		self.write("Hello, put node")

	def delete(self):
		self.write("Hello, delete node")

