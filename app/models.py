from _md5 import md5
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from app.getImage import getCityImage


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
    city = db.Column(db.String(140))
    description = db.Column(db.String(400))
    image = db.Column(db.String(140))
    flights = db.Column(db.PickleType(True))
    keywords = db.Column(db.PickleType(True))
    hotels = db.Column(db.PickleType(True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Recommendation {}>'.format(self.city)


class PastTrip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(140))
    image = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Recommendation {}>'.format(self.city)


class Favourite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(140))
    description = db.Column(db.String(400))
    image = db.Column(db.String(140))
    flights = db.Column(db.PickleType(True))
    keywords = db.Column(db.PickleType(True))
    hotels = db.Column(db.PickleType(True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Recommendation {}>'.format(self.city)



class CitiesToAvoid(db.Model):
    city = db.Column(db.String(140), primary_key=True)


class ProcessedCity(db.Model):
    city = db.Column(db.String(140), primary_key=True)
    country = db.Column(db.String(140))
    region = db.Column(db.String(140))
    keywords = db.Column(db.PickleType(True))
    sentiment = db.Column(db.Float)
    image = db.Column(db.String(140))
    description = db.Column(db.String(140))


