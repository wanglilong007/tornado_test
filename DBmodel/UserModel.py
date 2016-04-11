
from peewee import *
import SqliteBaseModel

class User(SqliteBaseModel.BaseModel):
	name = CharField()
	password = CharField()
	sex = CharField()
	birthday = DateField()
	address = CharField()
	statement = CharField()
