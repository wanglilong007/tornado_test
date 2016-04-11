
from peewee import *
#import UserModel.User
from UserModel import *

db = SqliteDatabase('love.db')

def create_tables():
	db.connect()
	db.create_tables([User])
