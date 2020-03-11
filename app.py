from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from app import app, db
from app.models import User, Recommendation
from app import routes
from app import models
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)
login.login_view = 'login'
bootstrap = Bootstrap(app)

db = SQLAlchemy()
db.init_app(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Recommendation': Recommendation}

if __name__ == "__main__":
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)