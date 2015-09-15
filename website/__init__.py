import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import Config
from flaskext.markdown import Markdown
import errors
from redis import StrictRedis


# redis client
r = StrictRedis(host='localhost', port=6379, db=0)

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

extension_configs = {
    'codehilite':
        {
            'guess_lang': False,

        }
}
Markdown(app, extensions=['extra', 'codehilite', 'website.utils.add_attribute'], output_format='html5',
         extension_configs=extension_configs)

errors.init_app(app)

#  Logging
import logging

logging.basicConfig(
    level=app.config['LOG_LEVEL'],
    format='%(asctime)s %(levelname)s: %(message)s '
           '[in %(pathname)s:%(lineno)d]',
    datefmt='%Y%m%d-%H:%M%p',

)

#  Email on errors
if not app.debug and not app.testing:
    import logging.handlers

    mail_handler = logging.handlers.SMTPHandler(
        'localhost',
        os.getenv('USER'),
        app.config['SYS_ADMINS'],
        '{0} error'.format(app.config['SITE_NAME']),
    )
    mail_handler.setFormatter(logging.Formatter('''
        Message type:       %(levelname)s
        Location:           %(pathname)s:%(lineno)d
        Module:             %(module)s
        Function:           %(funcName)s
        Time:               %(asctime)s
        Message:
        %(message)s
    '''.strip()))
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)
    app.logger.info("Emailing on error is ENABLED")
else:
    app.logger.info("Emailing on error is DISABLED")

# Email
from flask.ext.mail import Mail

app.mail = Mail(app)

# WTForms helpers
from utils import wtf

wtf.add_helpers(app)

# jinja filters
from utils.filters import add_filters

add_filters(app)

from views import *
