from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField, \
    SelectMultipleField, widgets, RadioField
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
    state = StringField('State', validators=[DataRequired()])
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



class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class KeywordsForm(FlaskForm):
    SelectMultipleField(choices=('family', 'wilderness', 'culinary', 'cultural', 'volunteer', 'solo',
                                 'adventure', 'self drive', 'accessible', 'last minute', 'snow', 'beach',
                                 'sight seeing', 'partying', 'cold', 'shopping', 'romantic', 'warm',
                                 'theme park', 'water sports', 'food'))
    submit = SubmitField('Submit')


class QuestionnaireForm(FlaskForm):
    currency = SelectField("Currency", choices=[("USD", "USD"), ("GBP", "GBP"), ("JP", "JP")],
                           validators=[DataRequired()])
    maxbudget = StringField('Max Budget', validators=[DataRequired()])
    minbudget = StringField('Min Budget', validators=[DataRequired()])
    adults = SelectField("Adults", choices=[("0", "0"), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")],
                         validators=[DataRequired()])
    children6 = SelectField("Children6", choices=[("0", "0"), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"),
                                                  ("5", "5")], validators=[DataRequired()])
    children612 = SelectField("Children612", choices=[("0", "0"), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"),
                                                      ("5", "5")], validators=[DataRequired()])
    children1218 = SelectField("Children1218", choices=[("0", "0"), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"),
                                                        ("5", "5")], validators=[DataRequired()])
    startDate = DateField('Start Date', validators=[DataRequired()])
    endDate = DateField('End Date', validators=[DataRequired()])
    localorabroad = RadioField('Destination', choices=[('local', 'local'), ('abroad', 'abroad')])
    origincountry = StringField('Country', validators=[DataRequired()])
    originstate = StringField('State', validators=[DataRequired()])
    submit = SubmitField('Submit')


class FavouritedForm(FlaskForm):
    submit = SubmitField('toggle-heart')

class ContactUsForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    query = StringField('Query', validators=[DataRequired()])



class EditProfileNameForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EditProfileAddressForm(FlaskForm):
    address = StringField('Address', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    postcode = StringField('Postcode', validators=[DataRequired()])
    submit = SubmitField('Submit')


class EditProfilePasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    newPassword = PasswordField('New Password')
    newPassword2 = PasswordField('Repeat New Password', validators=[EqualTo('newPassword')])
    submit = SubmitField('Submit')


class ForgotPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Submit')


