# -*- coding: utf-8 -*-
from website import db
from flask.ext.security import UserMixin, RoleMixin, SQLAlchemyUserDatastore
import datetime
from slugify import slugify
from sqlalchemy.dialects import postgresql


class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    slug = db.Column(db.String(64), unique=True)
    body = db.Column(db.UnicodeText)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, title=None, body=None):
        self.title = title
        self.body = body
        self.slug = slugify(title)

    def __unicode__(self):
        return self.title


tags_problems = db.Table(
    'tags_problems',
    db.Column('problem_id', db.Integer, db.ForeignKey('problem.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')))


class Tag(db.Model, RoleMixin):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    description = db.Column(db.String)

    def __unicode__(self):
        return self.name


class Problem(db.Model):
    __tablename__ = 'problem'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    slug = db.Column(db.String(64), unique=True)
    body = db.Column(db.UnicodeText)
    solution = db.Column(db.UnicodeText)
    count = db.Column(db.Integer, default=0)
    difficulty = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    tags = db.relationship(
        'Tag', secondary=tags_problems,
        backref=db.backref('problems', lazy='dynamic'))
    submissions = db.relationship('Submission', backref='problem', lazy='dynamic')
    test_cases = db.Column(postgresql.ARRAY(db.String))

    def __init__(self, title=None, body=None, solution=None,
                 difficulty=None, timestamp=None):
        self.title = title
        self.body = body
        self.solution = solution
        self.difficulty = difficulty
        self.slug = slugify(title)

        self.timestamp = timestamp

    def __unicode__(self):
        return self.title


roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    description = db.Column(db.String)

    def __unicode__(self):
        return self.name


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    username = db.Column(db.String(60), unique=True)
    confirmed_at = db.Column(db.DateTime())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(255))
    current_login_ip = db.Column(db.String(255))
    login_count = db.Column(db.Integer)
    time_registered = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    bio = db.Column(db.UnicodeText)
    avatar = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    roles = db.relationship(
        'Role', secondary=roles_users,
        backref=db.backref('users', lazy='dynamic'))
    problems = db.relationship('Problem', backref='author', lazy='dynamic')
    submissions = db.relationship('Submission', backref='user', lazy='dynamic')

    def __unicode__(self):
        return self.username


class Submission(db.Model):
    __tablename__ = 'submission'
    id = db.Column(db.Integer, primary_key=True)
    problem_id = db.Column(db.Integer, db.ForeignKey('problem.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    time = db.Column(db.Float)  # TODO string or float?
    code = db.Column(db.UnicodeText)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    successful = db.Column(db.Boolean)
    error = db.Column(db.String(255))

    def __unicode__(self):
        return str(self.id)


user_datastore = SQLAlchemyUserDatastore(db, User, Role)


def get_or_create(model, **kwargs):
    """SqlAlchemy implementation of Django's get_or_create.
    """
    session = db.session
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance
