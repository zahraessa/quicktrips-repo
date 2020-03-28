from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm, KeywordsForm, QuestionnaireForm, \
    FavouritedForm, ContactUsForm, EditProfileAddressForm, EditProfileNameForm, EditProfilePasswordForm, \
    ForgotPasswordForm
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Recommendation, ProcessedCity, CurrentRecommendation, CurrentQuestionnaire, Favourite
from datetime import datetime
from app.sendEmail import contactUsConfirmation, RegistrationConfirmation, ForgotPasswordEmail
from app.getAllInformationForARecommendation import getRecommendationInfo
from itsdangerous import URLSafeSerializer
from app.getImage import getCityImage


@app.route('/')
@app.route('/index')
def index():
    cities = ProcessedCity.query.all()
    i = 0
    recommendations1 = []
    recommendations2 = []
    if current_user.is_authenticated:
        recommendations = Recommendation.query.all()
        for recommendation in recommendations:
            if recommendation.user_id == current_user.id:
                i += 1
                if i < 4:
                    recommendations1.append(cities[i])
                if i in range(5, 9):
                    recommendations2.append(cities[i])
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
                                                description=description, image=getCityImage(c))
                    if i < 4:
                        recommendations1.append(rec)
                    else:
                        recommendations2.append(rec)
                    i += 1
                else:
                    break

    for x in CurrentQuestionnaire.query.all():
        db.session.delete(x)
    db.session.commit()
    return render_template("index.html", title='Home Page', recommendations1=recommendations1,
                           recommendations2=recommendations2)


# Login and register pages routing

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    # print(form.validate_on_submit())
    # print(form.submit.data)
    # print(request.method)
    if form.validate_on_submit():
        # print(form.username.data)
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
    # print("AAA")
    # print(form.validate_on_submit())
    # print(form.submit.data)
    if form.validate_on_submit():
        # print("HEREEEEE")
        user = User(username=form.username.data, email=form.email.data, firstname=form.firstname.data,
                    surname=form.surname.data, address=form.address.data, country=form.country.data,
                    city=form.state.data, postcode=form.postcode.data)
        user.set_password(form.password.data)
        user.avatar(128)
        db.session.add(user)
        db.session.commit()

        RegistrationConfirmation(name=form.firstname.data, username=form.username.data, email=form.username.data)

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
                    db.session.commit()

                    i += 1
                else:
                    break

        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('registerdone'))
    else:
        # print("BBB")
        return render_template('register.html', form=form)


@app.route('/forgetpw', methods=['GET', 'POST'])
def forgotPassword():
    form = ForgotPasswordForm()

    if form.validate_on_submit():
        user_id = 1
        password = "temp"

        auth_s = URLSafeSerializer('super-secret-key')
        token = auth_s.dumps([user_id, password])

        ForgotPasswordEmail("name", "email", "code")
        #
        print(token)
        # # eyJpZCI6NSwibmFtZSI6Iml0c2Rhbmdlcm91cyJ9.6YP6T0BaO67XP--9UzTrmurXSmg
        #
        # data = auth_s.loads(token)
        # print(data[0])
        # # itsdangerous
        return render_template('forgetpw.html', form=form)


# TODO: CREATE PAGE
@app.route('/forgetpwkey', methods=['GET', 'POST'])
def forgotPasswordkey():
    #
    # auth_s = URLSafeSerializer("secret key", "auth")
    # token = auth_s.dumps({"username": current_user.username})
    #
    # print(token)
    # # eyJpZCI6NSwibmFtZSI6Iml0c2Rhbmdlcm91cyJ9.6YP6T0BaO67XP--9UzTrmurXSmg
    #
    # data = auth_s.loads(token)
    # print(data["username"])
    # # itsdangerous
    return render_template('forgetpw.html')


# TODO: CREATE NEW PASSWORD PAGE
@app.route('/newpassword', methods=['GET', 'POST'])
def enterNewPassword():
    form = ForgotPasswordForm()
    #
    # auth_s = URLSafeSerializer("secret key", "auth")
    # token = auth_s.dumps({"id": current_user.id, "username": current_user.username})
    #
    # print(token)
    # # eyJpZCI6NSwibmFtZSI6Iml0c2Rhbmdlcm91cyJ9.6YP6T0BaO67XP--9UzTrmurXSmg
    #
    # data = auth_s.loads(token)
    # print(data["username"])
    # # itsdangerous
    return render_template('forgetpw.html', form=form)


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
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('userpage.html', user=user)


@app.route('/favourites/<username>')
@login_required
def favourites(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('userfavourite.html', user=user)


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
        current_user.city = form.state.data
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
    print("AA")
    print(form.firstname.data)
    print(form.surname.data)

    if request.method == "POST" and form.validate_on_submit():
        print("BB")
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
        oldanswers = CurrentQuestionnaire.query.first()
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
        return redirect(url_for('result', maxbudget=maxbudget,
                                minbudget=minbudget, adults=adults,
                                children=children, startdate=startdate,
                                enddate=enddate, triplength=triplength, localorabroad=localorabroad,
                                origin=origin, currency=currency, keywords=selected))
    return render_template('keyword.html', form=form, maxbudget=maxbudget,
                           minbudget=minbudget, adults=adults,
                           children=children, startdate=startdate,
                           enddate=enddate, triplength=triplength,
                           localorabroad=localorabroad, origin=origin, currency=currency)


@app.route('/result', methods=['GET', 'POST'])
def result():
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

    searchQueries = [maxbudget, minbudget, currency, adults, children, startdate, enddate, localorabroad, origin,
                     keywords]

    torecommend = getRecommendationInfo(origin=origin, adults=int(adults), children=int(children),
                                        startdate=startdate, enddate=enddate, currency=currency, triplength=triplength,
                                        keywords=keywords, localorinternational=localorabroad, maxbudget=maxbudget,
                                        minbudget=minbudget)
    if current_user.is_authenticated:
        db.session.query(Recommendation).filter(Recommendation.user_id == current_user.id).delete()
        db.session.commit()
        for x in torecommend:
            new = Recommendation(city=x, description=torecommend[x][2],
                                 flights=torecommend[x][0], keywords=torecommend[x][3],
                                 hotels=torecommend[x][1], user_id=current_user.id)
            db.session.add(new)
            db.session.commit()
        recommendations = db.session.query(Recommendation).filter(Recommendation.user_id == current_user.id).all()
    else:
        db.session.query(CurrentRecommendation).delete()
        db.session.commit()
        for x in torecommend:
            new = CurrentRecommendation(city=x, description=torecommend[x][2],
                                        flights=torecommend[x][0], keywords=torecommend[x][3],
                                        hotels=torecommend[x][1])
            db.session.add(new)
            db.session.commit()
        recommendations = CurrentRecommendation.query.all()
    numberOfRecommendation = (len(recommendations))
    return render_template('result.html', title='Result', recommendations=recommendations, currency=currency,
                           searchQueries=searchQueries, totalNumber=numberOfRecommendation)


@app.route('/details/<city>', methods=['GET', 'POST'])
def details(city):
    form = FavouritedForm()
    current_recommendation = []
    if current_user.is_authenticated:
        recommendations = db.session.query(Recommendation).filter(Recommendation.user_id == current_user.id)
    else:
        recommendations = CurrentRecommendation.query.all()

    flights = []
    hotels = []
    description = ""
    image = ""
    rec_id = 10000000000
    isFavourited = False

    for recommendation in recommendations:
        if recommendation.city == city:
            flights = recommendation.flights
            hotels = recommendation.hotels
            description = recommendation.description
            image = recommendation.image()
            rec_id = recommendation.id
            current_recommendation = recommendation
            isFavourited = recommendation.isFavourited()
            break
    return render_template('detail.html', city=city, recommendation=current_recommendation, hotels=hotels, recid=rec_id,
                           flights=flights, image=image, description=description, form=form, isFavourited=isFavourited)


@app.route('/favourites/favourite-details/<city>', methods=['GET', 'POST'])
def favouritedetails(city):
    form = FavouritedForm()
    current_recommendation = []
    favourites = db.session.query(Favourite).filter(Recommendation.user_id == current_user.id)

    flights = []
    hotels = []
    description = ""
    image = ""
    rec_id = 10000000000
    isFavourited = False

    for recommendation in favourites:
        if recommendation.city == city:
            flights = recommendation.flights
            hotels = recommendation.hotels
            description = recommendation.description
            image = recommendation.image()
            rec_id = recommendation.id
            current_recommendation = recommendation
            isFavourited = True
            break
    return render_template('detail.html', city=city, recommendation=current_recommendation, hotels=hotels, recid=rec_id,
                           flights=flights, image=image, description=description, form=form, isFavourited=isFavourited)


@app.route('/favourite/<recommendation_id>')
@login_required
def favouriteRecommendation_action(recommendation_id):
    recommendation = Recommendation.query.filter_by(id=recommendation_id).first_or_404()
    isFavourited = recommendation.isFavourited()
    if isFavourited == False:
        recommendation.favourite()
        db.session.commit()
    else:
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


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
