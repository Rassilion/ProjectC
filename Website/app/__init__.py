from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import Config
import errors

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

errors.init_app(app)

# WTForms helpers
from utils import wtf

wtf.add_helpers(app)

from views import *
