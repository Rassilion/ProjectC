from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import Config
from flaskext.markdown import Markdown
import errors

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

Markdown(app,extensions=['extra'],output_format='html5')

errors.init_app(app)

# WTForms helpers
from utils import wtf

wtf.add_helpers(app)

from views import *
