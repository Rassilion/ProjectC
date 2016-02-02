#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
from CodeJudge import db
from sqlalchemy.dialects import postgresql


class Problem(db.Model):
    __tablename__ = 'problem'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    author_id = db.Column(db.Integer)
    slug = db.Column(db.String(64), unique=True)
    body = db.Column(db.UnicodeText)
    solution = db.Column(db.UnicodeText)
    count = db.Column(db.Integer, default=0)
    difficulty = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    # removed tag reletionship
    submissions = db.relationship('Submission', backref='problem', lazy='dynamic')
    test_cases = db.Column(postgresql.ARRAY(db.String))

    def __unicode__(self):
        return self.title


class Submission(db.Model):
    __tablename__ = 'submission'
    id = db.Column(db.Integer, primary_key=True)
    problem_id = db.Column(db.Integer, db.ForeignKey('problem.id'))
    user_id = db.Column(db.Integer)
    time = db.Column(db.Float)
    code = db.Column(db.UnicodeText)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    successful = db.Column(db.Boolean)
    error = db.Column(db.String(255))

    def __repr__(self):
        return str(self.id)
