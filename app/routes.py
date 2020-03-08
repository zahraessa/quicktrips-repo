import flask_login
from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm, KeywordsForm, QuestionnaireForm, FavouritedDetailsForm
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Recommendation, Favourite
from app.getHotels import getHotelName, getHotelPhoto
from app.getCityDetails import getCityDescription
from app.getCountryDetails import getCountryDescription
import requests
import json
from app.getRandomCity import randomCityGenerator


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template("index.html", title='Home Page')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    print(form.validate_on_submit())
    print(form.submit.data)
    print(request.method)
    if form.validate_on_submit():
        print(form.username.data)
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    print("AAA")
    print(form.validate_on_submit())
    print(form.submit.data)
    print(request.method)
    if form.validate_on_submit():
        print("HEREEEEE")
        user = User(username=form.username.data, email=form.email.data, firstname=form.firstname.data,
                    surname=form.surname.data, address=form.address.data, country=form.country.data,
                    city=form.city.data, postcode=form.postcode.data)
        user.set_password(form.password.data)
        user.avatar(128)
        db.session.add(user)
        db.session.commit()
        placejson = randomCityGenerator()
        country = placejson[1]
        city = placejson[2]
        r = Recommendation(country=country, city=city, hotel1='Hilton', hotel2='Ibis', hotel3='Travelodge',
                           flight1='British Airways', flight2='Easy Jet', flight3='Turkish Airlines',
                           key_attraction='London Eye', description='London is a great place to visit', user_id=user.id)
        db.session.add(r)
        db.session.commit()
        placejson = randomCityGenerator()
        country = placejson[1]
        city = placejson[2]
        r = Recommendation(country=country, city=city, hotel1='Hilton', hotel2='Ibis', hotel3='Travelodge',
                           flight1='KLM', flight2='Air France', flight3='Ryan Air',
                           key_attraction='London Eye', description='Come see the Louvre!', user_id=user.id)
        db.session.add(r)
        db.session.commit()
        placejson = randomCityGenerator()
        country = placejson[1]
        city = placejson[2]
        r = Recommendation(country=country, city=city, hotel1='Four Seasons', hotel2='Emirates Hotel',
                           hotel3='Ibis', flight1='British Airways', flight2='Gulf Air', flight3='Emirates',
                           key_attraction='London Eye', description='Come see the worlds tallest building',
                           user_id=user.id)

        db.session.add(r)
        db.session.commit()
        placejson = randomCityGenerator()
        country = placejson[1]
        city = placejson[2]
        r = Recommendation(country=country, city=city, hotel1='Hotel Chalet Swiss',
                           hotel2='Grand Hotel National Luzern', hotel3='Travelodge', flight1='British Airways',
                           flight2='Easy Jet', flight3='Emirates', key_attraction='London Eye', description='Fresh Air',
                           user_id=user.id)

        db.session.add(r)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    else:
        print("BBB")
        return render_template('register.html', form=form)


@app.route('/userpage/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('userpage.html', user=user)


@app.route('/favourites/<username>')
@login_required
def favourites(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('userfavourite.html', user=user)


@app.route('/detail/<city>')
@login_required
def details(city):
    recommendations = Recommendation.query.all()
    for recommendation in recommendations:
        if recommendation.city == city:
            current_recommendation = recommendation
            break
        else:
            current_recommendation = recommendation
    form = FavouritedDetailsForm()
    a = request.form.get('toggle_heart.data')

    print(a)

    description = getCityDescription(city)
    hotel1name = getHotelName(recommendation.city, 0)
    hotel1photo = getHotelPhoto(recommendation.city, 0)
    hotel2name = getHotelName(recommendation.city, 1)
    hotel2photo = getHotelPhoto(recommendation.city, 1)
    hotel3name = getHotelName(recommendation.city, 2)
    hotel3photo = getHotelPhoto(recommendation.city, 2)
    if description == "":
        description = "country: " + recommendation.country
        for recommendation in recommendations:
            if recommendation.city == city:
                description = getCountryDescription(recommendation.country)
                hotel1name = getHotelName(recommendation.country, 0)
                hotel1photo = getHotelPhoto(recommendation.country, 0)
                hotel2name = getHotelName(recommendation.country, 1)
                hotel2photo = getHotelPhoto(recommendation.country, 1)
                hotel3name = getHotelName(recommendation.country, 2)
                hotel3photo = getHotelPhoto(recommendation.country, 2)
                break


    if a == True:
        newFavourite = Favourite(current_recommendation)
        db.session.add(newFavourite)
        db.session.commit()

    return render_template('detail.html', recommendation=current_recommendation,
                           description=description,
                           hotel1name=hotel1name,
                           hotel1photo=hotel1photo,
                           hotel2name=hotel2name,
                           hotel2photo=hotel2photo,
                           hotel3name=hotel3name,
                           hotel3photo=hotel3photo)


@app.route('/useredit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if request.method == "POST" and form.validate_on_submit():
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
        form.firstname.data = current_user.firstname
        form.surname.data = current_user.surname
        form.address.data = current_user.address
        form.country.data = current_user.country
        form.city.data = current_user.city
        form.postcode.data = current_user.postcode
    return render_template('useredit.html', title='Edit Profile', form=form)

@app.route('/usereditaddress')
def usereditaddress():
    return render_template('usereditaddress.html')


@app.route('/usereditemail')
def usereditemail():
    return render_template('usereditemail.html')


@app.route('/usereditname')
def usereditname():
    return render_template('usereditname.html')


@app.route('/usereditpassword')
def usereditpassword():
    return render_template('usereditpassword.html')


@app.route('/usereditphoto')
def usereditphoto():
    return render_template('usereditphoto.html')


@app.route('/usereditusername')
def usereditusername():
    return render_template('usereditusername.html')


@app.route('/result', methods=['GET', 'POST'])
@login_required
def result():
    recommendations = Recommendation.query.all()
    return render_template('result.html', title='Result', recommendations=recommendations)


@app.route('/forgetpw', methods=['GET', 'POST'])
def forgotPassword():
    return render_template('forgetpw.html')


@app.route('/googlelogin', methods=['GET', 'POST'])
def googlelogin():
    return render_template('googlelogin.html')


@app.route('/facebooklogin', methods=['GET', 'POST'])
def facebooklogin():
    return render_template('facebooklogin.html')


@app.route('/que', methods=['GET', 'POST'])
@login_required
def question():
    form = QuestionnaireForm()
    print(request.method)
    print(form.validate_on_submit())
    print(form.errors)
    print(form.localorabroad.data)
    if request.method == "POST" and form.validate_on_submit():
        maxcurrency = request.form.get('maxcurrency')
        mincurrency = request.form.get('mincurrency')
        maxbudget = request.form.get('maxbudget')
        minbudget = request.form.get('minbudget')
        adults = request.form.get('adults')
        children = request.form.get('children')
        startdate = request.form.get('startdate')
        enddate = request.form.get('enddate')
        triplength = request.form.get('triplength')
        localorabroad = request.form.get('localorabroad')
        print(maxbudget)
        print(minbudget)
        print(adults)
        print(children)
        print(startdate)
        print(enddate)
        print(triplength)
        print(localorabroad)
        #print(maxcurrency)
        #print(mincurrency)
        return redirect(url_for('keywords', maxbudget=maxbudget,
                                minbudget=minbudget, adults=adults,
                                children=children, startdate=startdate,
                                enddate=enddate, triplength=triplength,
                                localorabroad=localorabroad))
    return render_template('que.html', form=form)


@app.route('/keyword', methods=['GET', 'POST'])
@login_required
def keywords():
    form = KeywordsForm()
    maxbudget = request.args['maxbudget']
    minbudget = request.args['minbudget']
    #maxcurrency = request.args['maxcurrency']
    #mincurrency = request.args['mincurrency']
    adults = request.args['adults']
    children = request.args['children']
    startdate = request.args['startdate']
    enddate = request.args['enddate']
    triplength = request.args['triplength']
    localorabroad = request.args['localorabroad']
    if request.method == "POST" and form.validate_on_submit():
        selected = request.form.getlist('keywords')
        print(selected)
        return render_template('result.html', maxbudget=maxbudget,
                               minbudget=minbudget, adults=adults,
                               children=children, startdate=startdate,
                               enddate=enddate, triplength=triplength,
                               localorabroad=localorabroad)
    return render_template('keyword.html', form=form, maxbudget=maxbudget,
                           minbudget=minbudget, adults=adults,
                           children=children, startdate=startdate,
                           enddate=enddate, triplength=triplength,
                           localorabroad=localorabroad)

@app.route('/messagesent')
def messagesent():
    return render_template('messagesent.html')

@app.route('/contactus', methods=['GET', 'POST'])
def contactus():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        messages = request.form.get('messages')
        return redirect(url_for('messagesent'))
    return render_template('contactus.html')

@app.route('/emailsent')
def emailsent():
    return render_template('emailsent.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



