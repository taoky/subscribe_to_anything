from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_btn = SubmitField('Login')


class RegisterForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     EqualTo('confirm_password', message='passwords must match')])
    confirm_password = PasswordField('Confirm password')
    submit_btn = SubmitField('Register')


class ConfirmForm(Form):
    code = StringField('Confirm code', validators=[DataRequired()])
    submit_btn = SubmitField('Confirm')
