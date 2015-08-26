from sqlalchemy_wrapper import SQLAlchemy
from config import *

db = SQLAlchemy(SQLALCHEMY_DATABASE_URI)
