from application import app, db
from application.forms import ReviewerForm
from application.models import Reviews, Game
from flask import render_template, request, redirect, url_for

@app.route('/')
def index():
    all_games = Game.query.all()
    all_reviews = Reviews.query.all()
    return render_template('index.html', all_games=all_games, all_reviews=all_reviews)

@app.route('/added_game', methods=['GET', 'POST'])
def added_game():
    form = ReviewerForm()

    if request.method == 'POST':
        game = Game(game_name=form.game_name.data, description=form.description.data)
        db.session.add(game)
        db.session.commit()
        review = Reviews(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, review=form.review.data, game_id=game.id)
        db.session.add(review)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('added_game.html', form=form)

# form=form passes form = ReviewerForm to the added_game html page

@app.route('/delete/<int:id>/<int:id2>')
def delete_review(id, id2):
    review = Reviews.query.get(id2)
    db.session.delete(review)
    game = Game.query.get(id)
    db.session.delete(game)
    # db.session.commit()
    
    db.session.commit()
    return redirect(url_for('index'))