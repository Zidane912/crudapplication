from application import db
from datetime import datetime

class Reviewer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    game = db.relationship('Game', backref='reviewer')


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    game_name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    review = db.Column(db.String(100), nullable=False)
    date_review_place = db.Column(db.Datetime, nullable=False, default=datetime.now())
