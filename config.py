import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')

    SQLALCHEMY_TRACK_MODIFICATIONS = False