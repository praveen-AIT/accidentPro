# Imports
from app import db

# Create database
from models import Blogpost

db.create_all()

# Adding data
def add_post():
	print("working")
	db.session.add(Blogpost("AJAY","AFMC", 15))
	db.session.commit()
	print("DATA ADDED")


def get_input(name, hospital_name, hospital_dist):
	print("add_input working")
	name_str = str(name)
	hospital_name_str = str(hospital_name)
	dist_str = str(hospital_dist)
	
	db.session.add(Blogpost(name_str, hospital_name_str, dist_str))
	db.session.commit()