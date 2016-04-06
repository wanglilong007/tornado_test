
from peewee import *

db = SqliteDatabase('love.db')

class BaseModel(Model):
	class Meta:
		database = db

class User(BaseModel):
	name = CharField()
	password = CharField()
	sex = CharField()
	birthday = DateField()
	address = CharField()
	statement = CharField()

def create_tables():
	db.connect()
	db.create_tables([User])
