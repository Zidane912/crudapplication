from application import db

db.drop_all() # deletes db to refresh it
db.create_all() # recreates db