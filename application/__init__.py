from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import uuid

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")
app.config['SECRET_KEY'] = str(uuid.uuid4) # this was used because wtfforms uses CSRF to protect against unwanted forms being submitted
# this was done in this way so an environment varibale does not have to be used

# exported as an environment variable for security reasons by
# export DATABASE_URI=mysql+pymysql://root:*password set on gcvp*@*private ip of db on gcvp*/projectdb


db = SQLAlchemy(app)

from application import routes