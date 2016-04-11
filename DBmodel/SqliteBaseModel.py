
from peewee import *

db = SqliteDatabase('love.db')

class BaseModel(Model):
	class Meta:
		database = db
