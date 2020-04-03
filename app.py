from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from config import Config
from app.models import User, Recommendation
import psycopg2


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
bootstrap = Bootstrap(app)

from app import app

conn=psycopg2.connect(dbname='data', user='postgres', host='localhost', password='password', port=5432)

#db = SQLAlchemy()
#db.init_app(app)
db.create_all()
db.session.commit()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Recommendation': Recommendation}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
