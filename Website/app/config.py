import os


class Config():
    basedir = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'Impossible-to-guess-secret-code-that-you-will-never-guess!!!'

    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_PASSWORD_SALT = SECRET_KEY
    SECURITY_REGISTERABLE = True

    SECURITY_CONFIRMABLE = False
    SECURITY_RECOVERABLE = False
    SECURITY_TRACKABLE = False
    #no mail serv
    SECURITY_SEND_REGISTER_EMAIL=False

