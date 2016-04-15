import json
import tornado.web
import peewee

def db_conn(self):
	print('connect db\n')
