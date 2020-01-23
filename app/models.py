from _md5 import md5
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from app.getimage import getCityImage


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    firstname = db.Column(db.String(120), index=True)
    surname = db.Column(db.String(120), index=True)
    address = db.Column(db.String(120), index=True)
    country = db.Column(db.String(120), index=True)
    city = db.Column(db.String(120), index=True)
    postcode = db.Column(db.String(120), index=True)
    password_hash = db.Column(db.String(128))
    recommendations = db.relationship('Recommendation', backref='users', lazy='dynamic')
    favourites = db.relationship('Favourite', backref='users', lazy='dynamic')
    pastTrips = db.relationship('PastTrip', backref='users', lazy='dynamic')


    def __repr__(self):
        return '<User {}>'.format(self.email)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)



class Recommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(140))
    city = db.Column(db.String(140))
    hotel1 = db.Column(db.String(140))
    flight1 = db.Column(db.String(140))
    hotel2 = db.Column(db.String(140))
    flight2 = db.Column(db.String(140))
    hotel3 = db.Column(db.String(140))
    flight3 = db.Column(db.String(140))
    key_attraction = db.Column(db.String(140))
    description = db.Column(db.String(400))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Recommendation {}>'.format(self.city)

    def image(self, city):
        return getCityImage(city)


class PastTrip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(140))
    city = db.Column(db.String(140))
    hotel1 = db.Column(db.String(140))
    flight1 = db.Column(db.String(140))
    hotel2 = db.Column(db.String(140))
    flight2 = db.Column(db.String(140))
    hotel3 = db.Column(db.String(140))
    flight3 = db.Column(db.String(140))
    key_attraction = db.Column(db.String(140))
    description = db.Column(db.String(400))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Recommendation {}>'.format(self.city)

    def image(self, country):
        return getCityImage(country)


class Favourite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(140))
    city = db.Column(db.String(140))
    hotel1 = db.Column(db.String(140))
    flight1 = db.Column(db.String(140))
    hotel2 = db.Column(db.String(140))
    flight2 = db.Column(db.String(140))
    hotel3 = db.Column(db.String(140))
    flight3 = db.Column(db.String(140))
    key_attraction = db.Column(db.String(140))
    description = db.Column(db.String(400))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Recommendation {}>'.format(self.city)

    def image(self, country):
        return getCityImage(country)



