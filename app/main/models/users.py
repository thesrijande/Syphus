"""
DB Model for Users table and
Junction Table relating
Users and Tags
"""

from . import db
from enums import PriorityType
import datetime

class User(db.Model):
	"""
	Description of User model.
	Columns
	-----------
	:id: int [pk]	
	:username: varchar(128) [not NULL]
	:password: varchar(128) [not NULL]
	:first_name: varchar(255) [not NULL]
	:last_name: varchar(255)
	:dob: date
	:email: varchar(255) [not NULL]
	:fb_handle: varchar(255)
	:g_handle: varchar(255)
	:medium_handle: varchar(255)
	:twitter_handle: varchar(255)
	:linkedin_handle: varchar(255)
	:bio: text
	:occupation: varchar(255)
	:profile_picture: int
	:last_login: timestamp
	:creation_time: timestamp
	"""

	#Columns
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(128), nullable=False)
	password = db.Column(db.String(128), nullable=False)
	first_name = db.Column(db.String(255), nullable=False)
	last_name = db.Column(db.String(255), nullable=False)
	dob = db.Column(db.DateTime)
	email = db.Column(db.String(255), nullable=False)
	fb_handle = db.Column(db.String(255))
	g_handle = db.Column(db.String(255))
	medium_handle = db.Column(db.String(255))
	twitter_handle = db.Column(db.String(255))
	linkedin_handle = db.Column(db.String(255))
	profile_picture = db.Column(db.Integer)
	bio = db.Column(db.Text)
	occupation = db.Column(db.String(255))
	last_login = db.Column(db.DateTime)
	creation_time = db.Column(db.DateTime)

	#Relationships

	
	

#Junction Table relating Users and Tags
userTagJunction = db.Table('userTagJunction' ,
	db.Column('user_id', db.Integer,
		db.ForeignKey(user.id),primary_key = True) ,
	db.Column('keyword_id', db.Integer,db.ForeignKey(tag.id) ,
		primary_key = True) ,
	db.Column('priority' , db.Enum(PriorityType)))