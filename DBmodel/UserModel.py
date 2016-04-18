
from peewee import *
from SqliteBaseModel import *

class User(BaseModel):
	name = CharField()
	password = CharField()
	sex = CharField()
	birthday = DateField()
	address = CharField()
	statement = CharField()
