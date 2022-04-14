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

@app.route('/update/<int:id1>/<int:id2>', methods=['GET', 'POST'])
def update_review(id1, id2):
    review = Reviews.query.get(id1)
    game = Game.query.get(id2)
    form = ReviewerForm()

    if request.method == 'POST':
        game.game_name=form.game_name.data 
        game.description=form.description.data
        review.first_name=form.first_name.data
        review.last_name=form.last_name.data
        review.email=form.email.data
        review.review=form.review.data
        review.game_id=game.id
        db.session.commit()
        return redirect(url_for('index'))
    
    form.game_name.data=game.game_name
    form.description.data=game.description
    form.first_name.data=review.first_name
    form.last_name.data=review.last_name
    form.email.data=review.email
    form.review.data=review.review

# this last part is to repopulate the field which must be after the if statement otherwise the entry will remain its original data entry i.e. Red Dead would not change to Red Dead 2 if the user edits

    return render_template('added_game.html', form=form)

@app.route('/delete/<int:id1>/<int:id2>')
def delete_review(id1, id2):
    review = Reviews.query.get(id1)
    db.session.delete(review)
    game = Game.query.get(id2)
    db.session.delete(game)
    # db.session.commit()
    
    db.session.commit()
    return redirect(url_for('index'))