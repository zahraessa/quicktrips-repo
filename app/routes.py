from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm, KeywordsForm, QuestionnaireForm, \
    FavouritedForm, ContactUsForm, EditProfileAddressForm, EditProfileNameForm, EditProfilePasswordForm, ForgotPasswordForm
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Recommendation, Favourite, ProcessedCity
from app.getHotels import getHotelName, getHotelPhoto
from app.getCityDetails import getCityDescription
from app.getCountryDetails import getCountryDescription
from app.getRandomCity import randomCityGenerator
from app.getAllInformationForARecommendation import getRecommendationInfo
from datetime import date
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
        recommendations = current_user.recommendations
        for i in range(4):
            recommendations1.append(recommendations[i])
        for i in range(5, 9):
            recommendations2.append(recommendations[i])


    else:
        for city in cities:
            if city.keywords != [] and city.sentiment > 0.5:
                if i < 8:
                    c = city.city
                    image = getCityImage(city.city, city.country, city.region)
                    description = city.description
                    keywords = city.keywords
                    flights = []
                    hotels = []
                    rec = Recommendation(city=c, hotels=hotels, flights=flights, keywords=keywords,
                                         description=description, image=image, user_id="")

                    if i<4:
                        recommendations1.append(rec)
                    else:
                        recommendations2.append(rec)

                    i += 1
                else:
                    break
    return render_template("index.html", title='Home Page', recommendations1=recommendations1,
                           recommendations2=recommendations2)




#Login and register pages routing

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    #print(form.validate_on_submit())
    #print(form.submit.data)
    #print(request.method)
    if form.validate_on_submit():
        #print(form.username.data)
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
    #print("AAA")
    #print(form.validate_on_submit())
    #print(form.submit.data)
    if form.validate_on_submit():
        #print("HEREEEEE")
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
                    image = getCityImage(city.city, city.country, city.region)
                    description = city.description
                    keywords = city.keywords
                    flights = []
                    hotels = []
                    rec = Recommendation(city=c, hotels=hotels, flights=flights, keywords=keywords,
                                         description=description, image=image, user_id=user.id)

                    db.session.add(rec)
                    db.session.commit()

                    i += 1
                else:
                    break

        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('registerdone'))
    else:
        #print("BBB")
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


#TODO: CREATE PAGE
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


#TODO: CREATE NEW PASSWORD PAGE
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



#User Profile Routing

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





#Edit Profile Routing

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




#Questionnaire edit form routing

@app.route('/que', methods=['GET', 'POST'])
def question():
    form = QuestionnaireForm()
    # print(request.form.get('currency'))
    # print(request.method)
    # print(form.validate_on_submit())
    # print(form.errors)
    # print(form.localorabroad.data)
    if request.method == "POST":
        currency = request.form.get('currency')
        maxbudget = request.form.get('maxbudget')
        minbudget = request.form.get('minbudget')
        adults = request.form.get('adults')
        children = request.form.get('children6') + request.form.get('children612') + request.form.get('children1218')
        startdate = request.form.get('startDate')
        enddate = request.form.get('endDate')
        #TODO: Calculate trip length
        triplength = 5
        localorabroad = request.form.get('localorabroad')
        origincountry = request.form.get('origincountry')
        originstate = request.form.get('originstate')
        # print(maxbudget)
        # print(minbudget)
        # print(adults)
        # print(children)
        # print(startdate)
        # print(enddate)
        # print(triplength)
        # print(localorabroad)
        # print(origincountry)
        # print(originstate)
        # print(maxcurrency)
        # print(mincurrency)
        return redirect(url_for('keywords', currency=currency, maxbudget=maxbudget,
                                minbudget=minbudget, adults=adults,
                                children=children, startdate=startdate,
                                enddate=enddate, triplength=triplength,
                                localorabroad=localorabroad, origin=origincountry))
    return render_template('que.html', form=form)


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
    # print("AAAAA")
    # print(maxbudget)
    if request.method == "POST" and form.validate_on_submit():
        selected = request.form.getlist('keywords')
        #print(selected)

        # TODO: GET ORIGIN
        #print("RRRRRRRRRRRRRR")
        torecommend = getRecommendationInfo(origin=origin, numberOfPeople=(adults + children), startdate=startdate,
                                            enddate=enddate, currency=currency, triplength=triplength,
                                            keywords=selected, localorinternational=localorabroad)
        #print(len(torecommend))
        print("UMMMMMMM")
        print(torecommend)

        for x in torecommend:
            city = x  # city
            print("city: " + city)
            hotels = torecommend[x][1]  # hotels
            print("oooooo hotels: ")
            print(hotels)
            flights = torecommend[x][0]  # flights
            print("oooooo flights: ")
            print(flights)
            description = torecommend[x][2]  # Description
            image = torecommend[x][3]  # Photo
            keywords = torecommend[x][4]


        if current_user.is_authenticated:
            for recommendation in recommendations:
                if recommendation.user_id == current_user.id:
                    db.session.delete(recommendation)
                    db.session.commit()

            db.session.add(Recommendation(city=city, description=description,
                                          image=image, flights=flights,
                                          keywords=keywords, hotels=hotels,
                                          user_id=current_user.id))
            db.session.commit()



        return redirect(url_for('result', currency=currency, recommendations=torecommend))

    return render_template('keyword.html', form=form, maxbudget=maxbudget,
                           minbudget=minbudget, adults=adults,
                           children=children, startdate=startdate,
                           enddate=enddate, triplength=triplength,
                           localorabroad=localorabroad, origin=origin, currency=currency)






#Generate Recommendation Routing


@app.route('/result', methods=['GET', 'POST'])
def result():
    currency = request.args['currency']
    recommendations = request.args['recommendations']
    return render_template('result.html', title='Result', recommendations=recommendations, currency=currency)



@app.route('/details/<city>')
def details(city):
    isFavourited = False

    recommendations = Recommendation.query.all()

    for recommendation in recommendations:
        if recommendation.city == city:
            current_recommendation = recommendation
            break
        else:
            current_recommendation = recommendation

    favouritesList = Favourite.query.all()
    fave = []
    for favourite in favouritesList:
        if favourite.city == city:
            fave = favourite
            isFavourited = True
            break

    country = ""
    region = ""

    for processed in ProcessedCity.query.all():
        if processed.city == city:
            country = processed.country
            region = processed.country


    image = getCityImage(city, country, region)
    hotels = current_recommendation.hotels
    flights = current_recommendation.flights

    if current_user.is_authenticated:
        form = FavouritedForm()

        a = request.form.get('toggle_heart.data')
        #print(a)
        #print(form.submit.data)

        if form.submit.data == "True":
            if isFavourited:
                db.session.delete(fave)
                db.session.commit()
            else:
                newFavourite = Favourite(description=current_recommendation.description, city=current_recommendation.city,
                                         image=image, flights=current_recommendation.flights,
                                         hotels=current_recommendation.hotels, keywords=current_recommendation.keywords,
                                         user_id=current_user.id)
                db.session.add(newFavourite)
                db.session.commit()

    return render_template('detail.html', city=city, recommendation=current_recommendation, form=form,
                           isFavourited=isFavourited, hotels=hotels, flights=flights)





#misc pages routing

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
