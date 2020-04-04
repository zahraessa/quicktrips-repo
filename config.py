from os import environ as env
import multiprocessing
import os

from flask import Flask


class Config(object):
    app = Flask(__name__)

    PORT = int(env.get("PORT", 5000))
    DEBUG_MODE = int(env.get("DEBUG_MODE", 1))

    basedir = os.path.abspath(os.path.dirname(__file__))\

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                                   'sqlite:///' + os.path.join(basedir, 'app.db')


    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Gunicorn config
    bind = ":" + str(PORT)
    workers = multiprocessing.cpu_count() * 2 + 1
    threads = 2 * multiprocessing.cpu_count()




# import os
# basedir = os.path.abspath(os.path.dirname(__file__))\
#
# class Config(object):
#
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'password'
#
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
#                                'sqlite:///' + os.path.join(basedir, 'app.db')
#
#     #SQLALCHEMY_DATABASE_URI = 'postgres://admin:password@postgres:5432/demo_db'
#
#     #SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/quicktrips"
#
#     # user = 'admin'
#     # password = 'password'
#     # host = 'localhost'
#     # port = '5432'
#     # database = 'postgres'
#     #
#     #
#     #
#     # # user = os.environ['POSTGRES_USER']
#     # # password = os.environ['POSTGRES_PASSWORD']
#     # # host = os.environ['POSTGRES_HOST']
#     # # database = os.environ['POSTGRES_DB']
#     # # port = os.environ['POSTGRES_PORT']
#     #
#     # DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
#     #
#
#
#     # SQLALCHEMY_DATABASE_URI = DATABASE_CONNECTION_URI
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#
#
#
# # import os
# # basedir = os.path.abspath(os.path.dirname(__file__))
# #
# # class Config(object):
# #     SECRET_KEY = os.environ.get('SECRET_KEY') or 'password'
# #
# #     SQLALCHEMY_DATABASE_URI = 'postgres://dbadmin:12345@postgres:5432/demo_db'
# #
# #     SQLALCHEMY_TRACK_MODIFICATIONS = False