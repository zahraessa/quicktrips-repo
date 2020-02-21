import os
basedir = os.path.abspath(os.path.dirname(__file__))



class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'password'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False



# import os
# basedir = os.path.abspath(os.path.dirname(__file__))
#
# class Config(object):
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'password'
#
#     SQLALCHEMY_DATABASE_URI = 'postgres://dbadmin:12345@postgres:5432/demo_db'
#
#     SQLALCHEMY_TRACK_MODIFICATIONS = False