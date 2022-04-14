from flask_wtf import FlaskForm
# flaskform is the parent class where the the table classes will inherit from
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class ReviewerForm(FlaskForm):
    # id field not needed because it is a primary key so it auto-generated
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=50)])
    email = StringField('email', validators=[DataRequired()])
    game_name = StringField('Title', validators=[DataRequired(), Length(max=50)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(max=100)])
    review = TextAreaField('What do you think about this game?', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Submit Game Review')

# TextAreaField is used to make use of a larger text box as well as making using a longer length as this field
# would normally being longer than others

# class GameForm(FlaskForm): initially tried two forms but realised this would lead to two separate submit buttons
#     game_name = StringField('Title', validators=[DataRequired(), Length=(max=50)])
#     description = TextAreaField('Description', validators=[DataRequired(), Length=(max=100)])
#     review = TextAreaField('What do you think about this game?', validators=[DataRequired(), Length=(max=100)])

