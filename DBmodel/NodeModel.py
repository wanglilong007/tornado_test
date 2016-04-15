
from peewee import *
from SqliteBaseModel import *

class Node(BaseModel):
	name = CharField()
	ip = CharField()
	os = CharField()
