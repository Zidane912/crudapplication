from application import app, db
from application.forms import ReviewerForm
from application.models import Reviewer, Game
from flask import render_template, request

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/added_game', methods=['GET', 'POST'])
def added_game():
    form = ReviewerForm()

    if request.method == 'POST':
        reviewer = Reviewer(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, age=form.age.data)
        game = Game(game_name=form.game_name.data, description=form.description.data, review=form.review.data)
        db.session.add(reviewer)
        db.session.add(game)
        db.session.commit()
    return render_template('added_game.html', form=form)

# form=form passes form = ReviewerForm to the added_game html page