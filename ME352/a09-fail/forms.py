from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class Inputs(FlaskForm):
	m = DecimalField('Mass (kg)', places=2, validators=[DataRequired()])
	k = DecimalField('Spring Stiffness (N/m)', places=2, validators=[DataRequired()])
	z = DecimalField('Damping Ratio', places=3, validators=[DataRequired()])
	free = BooleanField("Free Vibration")
	forced = BooleanField("Forced Vibration")
	w = DecimalField('Forcing Harmonic Frequency (rad/s)', places=2)
	calc = SubmitField("Calculate")