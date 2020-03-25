from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField, SelectMultipleField, widgets, RadioField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, InputRequired
from app.models import User
from wtforms.fields.html5 import DateField

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    firstname = StringField('First Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    postcode = StringField('Postcode', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class EditProfileForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    postcode = StringField('Postcode', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    newPassword = PasswordField('New Password')
    newPassword2 = PasswordField('Repeat New Password', validators=[EqualTo('newPassword')])
    submit = SubmitField('Submit')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class KeywordsForm(FlaskForm):
    SelectMultipleField(choices=('family', 'wilderness', 'culinary', 'cultural', 'volunteer', 'solo',
                                           'adventure', 'selfdrive', 'accessible', 'lasminute', 'snow', 'beach',
                                           'signtseeing', 'partying', 'cold', 'shopping', 'romantic', 'warm',
                                           'themepark', 'watersports', 'food'))
    submit = SubmitField('Submit')

class QuestionnaireForm(FlaskForm):
    #maxcurrency = SelectField("Max Currency", choices=[("USD", "USD"), ("GBP", "GBP"), ("JPY", "JPY")], validators=[DataRequired()])
    #mincurrency = SelectField("Min Currency", choices=[("USD", "USD"), ("GBP", "GBP"), ("JPY", "JPY")], validators=[DataRequired()])
    maxbudget = StringField('Max Budget', validators=[DataRequired()])
    minbudget = StringField('Min Budget', validators=[DataRequired()])
    adults = StringField('Adults', validators=[DataRequired()])
    children = StringField('Children', validators=[DataRequired()])
    startdate = StringField('Start Date', validators=[DataRequired()])
    enddate = StringField('End Date', validators=[DataRequired()])
    triplength = StringField('Trip Length', validators=[DataRequired()])
    localorabroad = RadioField('Destination', choices=[('local', 'local'), ('abroad', 'abroad')])
    submit = SubmitField('Submit')

class FavouritedDetailsForm(FlaskForm):
    SelectField('toggle-heart', choices=[("Favourite", "Favourite"), ("Not-Favourite", "Not-Favourite")], validators=[InputRequired])