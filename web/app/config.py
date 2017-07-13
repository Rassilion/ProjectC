import os
import logging


class Config(object):
    # environment
    DEBUG = False
    TESTING = False
    PRODUCTION = False

    # log
    LOG_LEVEL = logging.DEBUG
    SYS_ADMINS = ['foo@example.com']
    SITE_NAME = 'ProjectC'

    basedir = os.path.abspath(os.path.dirname(__file__))
    REDIS_SERVICE = os.environ['REDIS_SERVICE']
    DB_NAME = os.environ['DB_NAME']
    DB_USER = os.environ['DB_USER']
    DB_PASS = os.environ['DB_PASS']
    DB_SERVICE = os.environ['DB_SERVICE']
    DB_PORT = os.environ['DB_PORT']
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
        DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
    )

    # form
    WTF_CSRF_ENABLED = True
    SECRET_KEY = os.environ['SECRET_KEY']
    PRODUCTS_PER_PAGE = 20

    # email server
    DEFAULT_MAIL_SENDER = 'Admin < username@example.com >'
    MAIL_SERVER = 'mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USE_SSL = False
    MAIL_USERNAME = '3780042a77f82155c'
    MAIL_PASSWORD = 'acffb68341777f'

    # security
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_PASSWORD_SALT = SECRET_KEY
    SECURITY_REGISTERABLE = True
    SECURITY_CONFIRMABLE = False
    SECURITY_RECOVERABLE = True
    SECURITY_TRACKABLE = True
    SECURITY_SEND_REGISTER_EMAIL = True
