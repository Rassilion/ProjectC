import os

basedir = os.path.abspath(os.path.dirname(__file__))
submissiondir = os.path.join(basedir, 'submissions')

REDIS_SERVICE = os.environ['REDIS_SERVICE']
DB_NAME = os.environ['DB_NAME']
DB_USER = os.environ['DB_USER']
DB_PASS = os.environ['DB_PASS']
DB_SERVICE = os.environ['DB_SERVICE']
DB_PORT = os.environ['DB_PORT']
SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
    DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
)
