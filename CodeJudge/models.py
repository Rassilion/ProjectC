import datetime
from CodeJudge import db


# basic Submission table no Foreign references
class Submission(db.Model):
    __tablename__ = 'submission'
    id = db.Column(db.Integer, primary_key=True)
    problem_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    time = db.Column(db.Integer)
    code = db.Column(db.UnicodeText)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    successful = db.Column(db.Boolean)
    error = db.Column(db.String(255))

    def __repr__(self):
        return str(self.id)
