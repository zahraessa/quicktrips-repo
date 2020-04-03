from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from config import Config
from app.models import User, Recommendation, ProcessedCity, CurrentRecommendation, CurrentQuestionnaire, \
    SharedRecommendations, PastTrip


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
bootstrap = Bootstrap(app)

from app import app

db.init_app(app)
db.create_all()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Recommendation': Recommendation}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
