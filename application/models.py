from application import db

class Reviewer(db.Model):
    id: db.Column(db.Integer, primary_key=True)
    first_name: db.Column(db.String(50), nullable=False)
    last_name: db.Column(db.String(50), nullable=False)
    email: db.Column(db.String(50), nullable=False)
    age: db.Column(db.Integer, nullable=False)