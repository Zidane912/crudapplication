from application import db
from datetime import datetime

# Table 1
class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    review = db.Column(db.String(100), nullable=False)
    date_review_placed = db.Column(db.DateTime, nullable=False, default=datetime.now())
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
# Here is where the first table connects to the table below

# Table 2
class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # game_id = db.Column(db.Integer(), db.ForeignKey('reviewer.id'), nullable=False) # here is the foregin key for the for the first table
    game_name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    review = db.relationship('Reviews', backref='game') # R is capital so that python knows about db rel, this is not for sql
    
    

# each review can review one game
# each game can have one-to-many reveiwers
# the relationship is one-to-many