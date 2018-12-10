from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class SubmissionForm(FlaskForm):
	sentence = TextAreaField()
	submit = SubmitField('Correct')