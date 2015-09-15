import os

basedir = os.path.abspath(os.path.dirname(__file__))
submissiondir = os.path.join(basedir, 'submissions')

SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
