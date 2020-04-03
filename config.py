from os import environ as env
import multiprocessing
import os


basedir = os.path.abspath(os.path.dirname(__file__))\

class Config(object):
    #general config
    PORT = int(env.get("PORT", 5000))
    DEBUG_MODE = int(env.get("DEBUG_MODE", 1))
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'password'

    def get_env_variable(name):
        try:
            return os.environ[name]
        except KeyError:
            message = "Expected environment variable '{}' not set.".format(name)
            raise Exception(message)

    # POSTGRES_USER = get_env_variable("POSTGRES_USER")
    # POSTGRES_PASSWORD = get_env_variable("POSTGRES_PASSWORD")
    # POSTGRES_DB = get_env_variable("POSTGRES_DB")
    # POSTGRES_HOST = get_env_variable("POSTGRES_HOST")
    # POSTGRES_PORT = get_env_variable("POSTGRES_PORT")
    # DB_URL = 'postgresql+psycopg2://{user}:{pw}@{host}:{port}/{db}'.format(user=POSTGRES_USER, pw=POSTGRES_PASSWORD,
    #                                                                host=POSTGRES_HOST, port=POSTGRES_PORT,
    #                                                                db=POSTGRES_DB)
    #SQLALCHEMY_DATABASE_URI = DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # SQLALCHEMY_DATABASE_URI = DB_URL

    SQLALCHEMY_DATABASE_URI ='postgres://postgres:password@postgres:5432/data'

    #'postgres://dbadmin:12345@postgres:5432/demo_db'


    #[DB_TYPE]+[DB_CONNECTOR]://[USERNAME]:[PASSWORD]@[HOST]:[PORT]/[DB_NAME]
    #
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #                           'sqlite:///' + os.path.join(basedir, 'app.db')

    # Gunicorn config
    bind = ":" + str(PORT)
    workers = multiprocessing.cpu_count() * 2 + 1
    threads = 2 * multiprocessing.cpu_count()