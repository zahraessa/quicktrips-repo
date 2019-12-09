from app import db

class Recommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cityname = db.Column(db.String(64), index=True, unique=True)
    countryname = db.Column(db.String(64), index=True, unique=False)
    body = db.Column(db.String(140))
    users = db.relationship('User', backref='userid', lazy='dynamic')

    def __repr__(self):
        return '<Post {}>'.format(self.body)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    city_id = db.Column(db.Integer, db.ForeignKey('recommendation.id'))

    def __repr__(self):
        return '<User {}>'.format(self.username)

