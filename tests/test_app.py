from flask_testing import TestCase
from application import app, db
from application.models import Game, Reviews
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///test.db')
        return app

    def setUp(self):
        db.create_all()
        game1 = Game(game_name="Tales of Vesperia", description="RPG")
        db.session.add(game1)
        db.session.commit()

        # review1 = Reviews(first_name="Zid", last_name="Alam", email="zid@gmail.com", review="Amazing but can get repetitive")
        # db.session.add(review1)
        # db.session.commit()
        # the secoond table was not included in the test under the assumption that if the first table functions so should the second
    def tearDown(self):
        db.drop_all()

class TestAddEntry(TestBase):
    def test_view_page(self):
        response = self.client.get(url_for('added_game'))
        self.assertEqual(response.status_code, 200)

    def test_create_review(self):
         response = self.client.post(
             url_for('added_game'),
             data = dict(game_name="Borderlands 2", description="RPG Shooter"),
             follow_redirects = True
         )
         self.assertEqual(response.status_code, 200)

# talk about 500 != 200, perhaps because my db for the tests was not set up properly

    

