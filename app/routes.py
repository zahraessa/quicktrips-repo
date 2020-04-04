from flask import render_template, flash, redirect, url_for, request, jsonify
from app import app, db
from app.forms import LoginForm, RegistrationForm, KeywordsForm, QuestionnaireForm, ForgotPasswordForm,\
    ContactUsForm, EditProfileAddressForm, EditProfileNameForm, EditProfilePasswordForm, PastTripForm,\
    ForgotPasswordCode, ForgotPasswordNewPassword
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Recommendation, ProcessedCity, CurrentRecommendation, CurrentQuestionnaire, \
    SharedRecommendations, PastTrip
from datetime import datetime
from app.sendEmail import contactUsConfirmation, RegistrationConfirmation, ForgotPasswordEmail
from app.getAllInformationForARecommendation import getRecommendationInfo
from itsdangerous import URLSafeSerializer
from app.getImage import getCityImage
import random
from random import randint
from socket import SocketIO
import time
from urllib.parse import quote, urlencode
import urllib
import json


@app.route('/')
@app.route('/index')
def index():
    cities = ProcessedCity.query.all()
    i = 0
    recommendations1 = []
    recommendations2 = []
    if current_user.is_authenticated:
        recommendations = db.session.query(Recommendation).filter_by(user_id=current_user.id).all()
        for recommendation in recommendations:
            i += 1
            if i < 4:
                recommendations1.append(recommendation.city)
            if i in range(5, 9):
                recommendations2.append(recommendation.city)
            else:
                break
    else:
        for city in cities:
            if city.keywords != [] and city.sentiment > 0.5:
                if i < 8:
                    c = city.city
                    description = city.description
                    keywords = city.keywords
                    flights = []
                    hotels = []
                    rec = CurrentRecommendation(city=c, hotels=hotels, flights=flights, keywords=keywords,
                                                description=description)
                    db.session.add(rec)
                    db.session.commit()
                    if i < 4:
                        recommendations1.append(rec)
                    else:
                        recommendations2.append(rec)
                    i += 1
                else:
                    break

    try:
        for x in CurrentQuestionnaire.query.all():
            db.session.delete(x)
        db.session.commit()
        return render_template("index.html", title='Home Page', recommendations1=recommendations1,
                               recommendations2=recommendations2)
    except:
        pass
    return render_template("index.html", title='Home Page', recommendations1=recommendations1,
                           recommendations2=recommendations2)


# Login and register pages routing

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            flash("Username is not recorded, please register before login!")
        elif not user.check_password(form.password.data):
            flash("Password entered does not match your username!")
        else:
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
    print("UMM")
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print("HEREEEE")
        def get_random_string(length=24,
                              allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
            return ''.join(random.choice(allowed_chars) for i in range(length))
        hashCode = get_random_string()
        print(hashCode)
        user = User(username=form.username.data, email=form.email.data, firstname=form.firstname.data,
                    surname=form.surname.data, address=form.address.data, country=form.country.data,
                    city=form.state.data, postcode=form.postcode.data, hashCode=hashCode)
        if user.username is not None:
            flash("Username has already been used by someone, please change the username!")
        if user.email is not None:
            flash("This email has already been registered, please change a email or login!")
        user.set_password(form.password.data)
        user.avatar(128)
        db.session.add(user)
        RegistrationConfirmation(name=form.firstname.data, username=form.username.data, email=form.username.data, code=hashCode)
        print("HERREE")
        cities = ProcessedCity.query.all()
        i = 0
        for city in cities:
            if city.keywords != [] and city.sentiment > 0.5:
                if i < 8:
                    c = city.city
                    description = city.description
                    keywords = city.keywords
                    flights = []
                    hotels = []
                    rec = Recommendation(city=c, hotels=hotels, flights=flights, keywords=keywords,
                                         description=description, user_id=user.id)
                    db.session.add(rec)
                    i += 1
                else:
                    break
        return redirect(url_for('confirmRegistration'), user=user)
    return render_template('register.html', form=form)


@app.route('/registerconfirmation', methods=['GET', 'POST'])
def confirmRegistration():
    form = ForgotPasswordCode()
    user = request.args['user']
    print(form.validate_on_submit())
    print(form.code.data)
    if form.validate_on_submit():
        code = form.code.data
        print(code)
        hashCode = user.hashCode
        if code == hashCode:
            db.session.commit()
            return redirect(url_for('registerdone'))
        else:
            flash("Incorrect token")
    return render_template('resetpwcode.html', form=form)



#TODO: FORGOT PASSWORD - Unique Code - New page
@app.route('/forgetpw', methods=['GET', 'POST'])
def forgotPassword():
    form = ForgotPasswordForm()

    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        def get_random_string(length=24,
                              allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
            return ''.join(random.choice(allowed_chars) for i in range(length))
        hashCode = get_random_string()
        user.hashCode = hashCode
        db.session.commit()

        ForgotPasswordEmail(user.username, email, hashCode)

        return redirect(url_for('forgotPasswordkey', email=email))

    return render_template('forgetpw.html', form=form)


# TODO: CREATE PAGE
@app.route('/forgetpwkey', methods=['GET', 'POST'])
def forgotPasswordkey():
    form = ForgotPasswordCode()
    email = request.args['email']
    print(form.validate_on_submit())
    print(form.code.data)
    if form.validate_on_submit():
        code = form.code.data
        print(code)
        user = User.query.filter_by(email=email).first()
        hashCode = user.hashCode
        if code == hashCode:
            return redirect(url_for('enterNewPassword', email=email, hashCode=hashCode))
        else:
            flash("Incorrect token")
    return render_template('resetpwcode.html', form=form)


# TODO: CREATE NEW PASSWORD PAGE
@app.route('/newpassword', methods=['GET', 'POST'])
def enterNewPassword():
    form = ForgotPasswordNewPassword()
    email = request.args['email']
    hashCode = request.args['hashCode']
    user = User.query.filter_by(email=email).first()
    if user.hashCode != hashCode:
        flash("Invalid Password Reset Link")
    if form.validate_on_submit():
        password = form.password.data
        print(user)
        user.set_password(password)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('resetpw.html', form=form)


@app.route('/googlelogin', methods=['GET', 'POST'])
def googlelogin():
    return render_template('googlelogin.html')


@app.route('/facebooklogin', methods=['GET', 'POST'])
def facebooklogin():
    return render_template('facebooklogin.html')


# User Profile Routing

@app.route('/userpage/<username>', methods=['GET', 'POST'])
@login_required
def user(username):
    form = PastTripForm()
    user = User.query.filter_by(username=username).first_or_404()
    if form.validate_on_submit():
        country = form.country.data
        rating = form.rate.data
        toAdd = PastTrip(country=country, rating=rating, user_id=current_user.id)
        db.session.add(toAdd)
        db.session.commit()
    countrylist = ""
    ratingslist = ""
    trips = PastTrip.query.filter_by(user_id=current_user.id).all()
    trips = set(trips)
    i = 0
    for trip in trips:
        i += 1
        countrylist += trip.country
        countrylist += ","
        ratingslist += trip.rating
        ratingslist += ","
    if len(countrylist) > 0:
        countrylist = countrylist[:-1]
        ratingslist = ratingslist[:-1]
    return render_template('userpage.html', user=user, form=form, countrylist=countrylist, ratingslist=ratingslist)


@app.route('/favourites/<username>')
@login_required
def favourites(username):
    print("faves")
    user = User.query.filter_by(username=username).first_or_404()
    favourites = Recommendation.query.filter_by(isFavourited=True).all()
    print(favourites)
    return render_template('userfavourite.html', user=user, favourites=favourites)


# Edit Profile Routing
@app.route('/useredit', methods=['GET', 'POST'])
@login_required
def useredit():
    return render_template('useredit.html', title='Edit Profile')


@app.route('/usereditaddress')
def usereditaddress():
    form = EditProfileAddressForm()
    if request.method == "POST" and form.validate_on_submit():
        current_user.address = form.address.data
        current_user.country = form.country.data
        current_user.city = form.city.data
        current_user.postcode = form.postcode.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('useredit'))
    elif request.method == 'GET':
        form.address.data = current_user.address
        form.country.data = current_user.country
        form.city.data = current_user.city
        form.postcode.data = current_user.postcode
    return render_template('usereditaddress.html', form=form)


@app.route('/usereditname', methods=['GET', 'POST'])
def usereditname():
    form = EditProfileNameForm()
    if request.method == "POST" and form.validate_on_submit():
        current_user.firstname = form.firstname.data
        current_user.surname = form.surname.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('useredit'))
    elif request.method == 'GET':
        form.firstname.data = current_user.firstname
        form.surname.data = current_user.surname
    return render_template('usereditname.html', form=form)


@app.route('/usereditpassword', methods=['GET', 'POST'])
def usereditpassword():
    form = EditProfilePasswordForm()
    if request.method == "POST" and form.validate_on_submit() and current_user.check_password(form.password.data):
        current_user.set_password(form.newPassword.data)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('useredit'))
    return render_template('usereditpassword.html', form=form)


# Questionnaire edit form routing
@app.route('/que', methods=['GET', 'POST'])
def question():
    form = QuestionnaireForm()
    if request.method == 'GET':
        try:
            oldanswers = CurrentQuestionnaire.query.first()
        except:
            pass
        if oldanswers is not None:
            form.currency.data = oldanswers.currency
            form.maxbudget.data = oldanswers.maxbudget
            form.minbudget.data = oldanswers.minbudget
            form.adults.data = oldanswers.adults
            form.children6.data = oldanswers.children6
            form.children612.data = oldanswers.children612
            form.children1218.data = oldanswers.children1218
            form.startDate = oldanswers.startdate
            form.endDate = oldanswers.enddate
            form.localorabroad = oldanswers.localorabroad
            form.origincountry = oldanswers.origincountry
            form.originstate = oldanswers.originstate
        return render_template('que.html', form=form)
    else:
        currency = request.form.get('currency')
        maxbudget = request.form.get('maxbudget')
        minbudget = request.form.get('minbudget')
        adults = request.form.get('adults')
        children = int(request.form.get('children6')) + int(request.form.get('children612')) + \
                   int(request.form.get('children1218'))
        startdate = request.form.get('startDate')
        enddate = request.form.get('endDate')
        localorabroad = request.form.get('localorabroad')
        origincountry = request.form.get('origincountry')
        originstate = request.form.get('originstate')
        q = CurrentQuestionnaire(currency=currency, maxbudget=maxbudget, minbudget=minbudget, adults=adults,
                                 children6=request.form.get('children6'), children612=request.form.get('children612'),
                                 children1218=request.form.get('children1218'), startdate=startdate, enddate=enddate,
                                 localorabroad=localorabroad, origincountry=origincountry, originstate=originstate)
        for x in CurrentQuestionnaire.query.all():
            db.session.delete(x)
        db.session.commit()
        db.session.add(q)
        db.session.commit()
        formatDate = '%Y-%m-%d'
        triplength = datetime.strptime(enddate, formatDate) - datetime.strptime(startdate, formatDate)
        return redirect(url_for('keywords', currency=currency, maxbudget=maxbudget,
                                minbudget=minbudget, adults=adults,
                                children=children, startdate=startdate,
                                enddate=enddate, triplength=triplength,
                                localorabroad=localorabroad, origin=origincountry))


@app.route('/keyword', methods=['GET', 'POST'])
def keywords():
    form = KeywordsForm()
    maxbudget = request.args['maxbudget']
    minbudget = request.args['minbudget']
    currency = request.args['currency']
    adults = request.args['adults']
    children = request.args['children']
    startdate = request.args['startdate']
    enddate = request.args['enddate']
    triplength = request.args['triplength']
    localorabroad = request.args['localorabroad']
    origin = request.args['origin']
    if request.method == "POST" and form.validate_on_submit():
        selected = request.form.getlist('keywords')
        return redirect(url_for('generateResults', maxbudget=maxbudget,
                           minbudget=minbudget, adults=adults,
                           children=children, startdate=startdate,
                           enddate=enddate, triplength=triplength,
                           localorabroad=localorabroad, origin=origin, currency=currency, keywords=selected))
    return render_template('keyword.html', form=form, maxbudget=maxbudget,
                           minbudget=minbudget, adults=adults,
                           children=children, startdate=startdate,
                           enddate=enddate, triplength=triplength,
                           localorabroad=localorabroad, origin=origin, currency=currency)


@app.route("/generateResults")
def generateResults():
    maxbudget = request.args['maxbudget']
    minbudget = request.args['minbudget']
    currency = request.args['currency']
    adults = request.args['adults']
    children = request.args['children']
    startdate = request.args['startdate']
    enddate = request.args['enddate']
    triplength = request.args['triplength']
    localorabroad = request.args['localorabroad']
    origin = request.args['origin']
    keywords = request.args.getlist('keywords')

    print("KEY")
    print(keywords)

    keywordsStr = ""

    for keyword in keywords:
        keywordsStr += keyword
        keywordsStr += "-"

    keywordsStr = keywordsStr[:-1]


    return render_template('loading.html', currency=currency, maxbudget=maxbudget,
                                minbudget=minbudget, adults=adults,
                                children=children, startdate=startdate,
                                enddate=enddate, triplength=triplength,
                                localorabroad=localorabroad, origin=origin, keywords=keywordsStr)

    # query_params = {'data': ','.join([maxbudget, minbudget, currency, adults, children, startdate, enddate,
    #                                  triplength, localorabroad, origin, keywords])}
    # query_string = urllib.parse.urlencode(query_params)
    # return render_template('loading.html', my_data=query_string)




@app.route("/processing")
def processing():
    maxbudget = request.args['maxbudget']
    minbudget = request.args['minbudget']
    currency = request.args['currency']
    adults = request.args['adults']
    children = request.args['children']
    startdate = request.args['startdate']
    enddate = request.args['enddate']
    triplength = request.args['triplength']
    localorabroad = request.args['localorabroad']
    origin = request.args['origin']
    keywordsString = request.args['keywords']
    #keywords = request.args.getlist('keywords')

    print(maxbudget)
    print(keywordsString)
    keywordsString = keywordsString[:-1]

    keywords = str.split(keywordsString, '-')
    print(keywords)

    torecommend = getRecommendationInfo(origin=origin, adults=int(adults), children=int(children),
                                        startdate=startdate, enddate=enddate, currency=currency, triplength=triplength,
                                        keywords=keywords, localorinternational=localorabroad, maxbudget=maxbudget,
                                        minbudget=minbudget)
    if current_user.is_authenticated:
        db.session.commit()
        for x in torecommend:
            new = Recommendation(city=x, description=torecommend[x][2],
                                 flights=torecommend[x][0], keywords=torecommend[x][3],
                                 hotels=torecommend[x][1], user_id=current_user.id, isFavourited=False)
            db.session.add(new)
            db.session.commit()
        recommendations = db.session.query(Recommendation).filter_by(user_id=current_user.id).all()
    else:
        db.session.query(CurrentRecommendation).delete()
        db.session.commit()
        for x in torecommend:
            new = CurrentRecommendation(city=x, description=torecommend[x][2],
                                        flights=torecommend[x][0], keywords=torecommend[x][3],
                                        hotels=torecommend[x][1], isFavourited=False)
            db.session.add(new)
            db.session.commit()
        recommendations = CurrentRecommendation.query.all()
    numberOfRecommendations = (len(recommendations))

    ids = []

    for recommendation in recommendations:
        ids.append(recommendation.id)


    return redirect(url_for('resultspage', recommendations=ids, currency=currency,
                           totalNumber=numberOfRecommendations))


@app.route('/resultspage', methods=['GET', 'POST'])
def resultspage():
    ids = request.args.getlist('recommendations')
    currency = request.args['currency']
    totalNumber = request.args['totalNumber']

    recommendations = []

    for id in ids:
        recommendation = Recommendation.query.filter_by(id=id).first_or_404()
        recommendations.append(recommendation)

    return render_template('result.html', title='Result', recommendations=recommendations, currency=currency,
                           totalNumber=totalNumber)



@app.route('/details/<city>', methods=['GET', 'POST'])
def details(city):
    current_recommendation = []
    recommendations = []
    if current_user.is_authenticated:
        recommendations = db.session.query(Recommendation).filter_by(user_id=current_user.id)
    else:
        recommendations = CurrentRecommendation.query.all()
    flights = []
    hotels = []
    description = ""
    image = ""
    rec_id = 10000000000
    isFavourited = False
    url = ""
    code = 0
    for recommendation in recommendations:
        if recommendation.city == city:
            flights = recommendation.flights
            hotels = recommendation.hotels
            description = recommendation.description
            image = recommendation.image()
            rec_id = recommendation.id
            current_recommendation = recommendation
            if current_user.is_authenticated:
                isFavourited = recommendation.isFavourited
                print(isFavourited)

            def get_random_string(length=24,
                                  allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
                return ''.join(random.choice(allowed_chars) for i in range(length))

            code = get_random_string()
            url = "shared/" + city + "/" + code
            toShare = SharedRecommendations(city=city, description=description, flights=flights, hotels=hotels,
                                            keywords=keywords, code=code)
            db.session.add(toShare)
            db.session.commit()
            break
    return render_template('detail.html', city=city, recommendation=current_recommendation, hotels=hotels, recid=rec_id,
                           flights=flights, image=image, description=description, isFavourited=isFavourited,
                           toShare=code)


@app.route('/favourites/favourite-details/<city>', methods=['GET', 'POST'])
def favouritedetails(city):
    current_recommendation = []
    favourites = db.session.query(Recommendation).filter_by(city=city)
    flights = []
    hotels = []
    description = ""
    image = ""
    rec_id = 10000000000
    isFavourited = False
    code = 0
    for recommendation in favourites:
        if recommendation.city == city and recommendation.user_id == current_user.id:
            flights = recommendation.flights
            hotels = recommendation.hotels
            description = recommendation.description
            image = recommendation.image()
            rec_id = recommendation.id
            current_recommendation = recommendation
            isFavourited = recommendation.isFavourited
            print(isFavourited)
            code = randint(0, 2147483647)
            url = "shared/" + city + "/" + str(code)
            toShare = SharedRecommendations(city=city, description=description, flights=flights, hotels=hotels,
                                            keywords=keywords, code=code)
            db.session.add(toShare)
            db.session.commit()
            break
    return render_template('detail.html', city=city, recommendation=current_recommendation, hotels=hotels, recid=rec_id,
                           flights=flights, image=image, description=description, isFavourited=isFavourited,
                           toShare=code)


@app.route('/shared/<city>/<identifier>', methods=['GET', 'POST'])
def sharedRecommendationDetails(city, identifier):
    isFavourited = False
    recommendations = db.session.query(SharedRecommendations).filter_by(code=identifier)
    code = 0
    for current_recommendation in recommendations:
        if current_recommendation.city == city:
            flights = current_recommendation.flights
            hotels = current_recommendation.hotels
            description = current_recommendation.description
            image = current_recommendation.image()
            rec_id = current_recommendation.id
            if current_user.is_authenticated:
                isFavourited = current_recommendation.isFavourited
            url = "shared/" + city + "/" + identifier
            return render_template('detail.html', city=city, recommendation=current_recommendation, hotels=hotels,
                                   recid=rec_id, flights=flights, image=image, description=description,
                                   isFavourited=isFavourited, toShare=code)
    return render_template('404.html')


@app.route('/favourite/<recommendation_id>')
@login_required
def favouriteRecommendation_action(recommendation_id):
    recommendation = Recommendation.query.filter_by(id=recommendation_id).first_or_404()
    print(recommendation)

    if recommendation is None or not recommendation.isFavourited:
        print("HERE")
        recommendation.favourite()
        db.session.commit()
    else:
        print("UMM")
        recommendation.unfavourite()
        db.session.commit()
    return redirect(request.referrer)


# misc pages routing
@app.route('/messagesent')
def messagesent():
    return render_template('messagesent.html')


@app.route('/contactus', methods=['GET', 'POST'])
def contactus():
    form = ContactUsForm()
    if request.method == 'POST':
        name = request.form.get('username')
        email = request.form.get('email')
        query = request.form.get('messages')
        contactUsConfirmation(name, email, query)
        return redirect(url_for('messagesent'))
    return render_template('contactus.html', form=form)


@app.route('/emailsent')
def emailsent():
    return render_template('emailsent.html')


@app.route('/registerdone')
def registerdone():
    return render_template('registerdone.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/emailconfirmation')
def email_confirm():
    return render_template('emailconfirmation.html')


@app.route('/resetpw')
def reset_password():
    return render_template('resetpw.html')


@app.route('/resetpwcode')
def reset_password_code():
    return render_template('resetpwcode.html')



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
