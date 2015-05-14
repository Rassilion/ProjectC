from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# WTForms helpers
from utils import wtf

wtf.add_helpers(app)

from views import *