from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")
# exported as an environment variable for security reasons by
# export DATABASE_URI=mysql+pymysql://root:*password set on gcvp*@*private ip of db on gcvp*/projectdb

db = SQLAlchemy(app)

from application import routes