import flask_login
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask import request
from werkzeug.urls import url_parse
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask_login import login_required
from app import db
from app.forms import RegistrationForm
from app.forms import EditProfileForm


@app.route('/')
@app.route('/index')
@login_required
def index():
    recommendations = [
        {
            'recommendation': {'place': 'London'},
            'city': 'London',
            'body': "London Eye, Big Ben",
            'image': "London.png"
        },
        {
            'recommendation': {'place': 'New York'},
            'city': 'New York',
            'body': "Empire State Building",
            'image': "newyork.png"
        },
        {
            'recommendation': {'place': 'Dubai'},
            'city': 'Dubai',
            'body': "Burj Al Arab",
            'image': "dubai.png"
        }
    ]
    return render_template("index.html", title='Home Page', recommendations=recommendations)


@app.route('/login', methods=['GET', 'POST'])
def login():
    print(request.method)
    print('1')
    if current_user.is_authenticated:
        print('2')
        return redirect(url_for('index'))
    form = LoginForm()
    print('3')
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print('4')
        user = User.query.filter_by(username=form.username.data).first()
        print(form.username.data)
        print(form.password.data)
        if user is None or not user.check_password(form.password.data):
            print('5')
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            print('6')
            next_page = url_for('index')
        return redirect(next_page)
    print('7')
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    print('1')
    if current_user.is_authenticated:
        print('2')
        return redirect(url_for('index'))
    print('3')
    form = RegistrationForm()
    print(form.firstname.data)
    if form.validate_on_submit():
        print('4')
        user = User(username=form.username.data, email=form.email.data, firstname=form.firstname.data,
        surname=form.surname.data, address=form.address.data, country=form.country.data, city=form.city.data,
        postcode = form.postcode.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    print('5')
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    recommendations = [
        {'city': user, 'body': 'Test post #1'},
        {'city': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, recommendations=recommendations)



@app.route('/useredit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    print('hereee')
    if form.validate_on_submit() and current_user.check_password(form.password.data):
        print('sjsjjsk')
        current_user.firstname = form.firstname.data
        current_user.surname = form.surname.data
        current_user.address = form.address.data
        current_user.country = form.country.data
        current_user.city = form.city.data
        current_user.postcode = form.postcode.data
        current_user.set_password(form.newPassword.data)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('index'))
    elif request.method == 'GET':
        print('loool')
    return render_template('useredit.html', title='Edit Profile', form=form)





@app.route('/question', methods=['GET', 'POST'])
def question():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Questionnaire requested for user {}, holidaytype={}, budgetmin={}, budgetmax={}, nochildren={}, noadults={}, datestart={}, dateend={}, length={}, destination={}, interests={}'.format(
            form.username.data, form.holidaytype.data, form.budgetmin.data, form.budgetmax.data, form.nochildren.data, form.noadults.data, form.datestart.data, form.dateend.data, form.length.data, form.destination.data, form.interest.data))
        return redirect('/index')
    return render_template('question.html', title='Questionnaire', form=form)
