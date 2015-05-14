# -*- coding: utf-8 -*-
from app import db
from flask.ext.security import UserMixin, RoleMixin
import datetime
from slugify import slugify


class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    slug = db.Column(db.String(64), unique=True)
    body = db.Column(db.String, unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, title=None, body=None):
        self.title = title
        self.body = body
        self.slug = slugify(title) #hata kontrolu ekle


    def __repr__(self):
        return '<News %r>' % (self.title)


class Problems(db.Model):
    __tablename__ = 'problems'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    slug = db.Column(db.String(64), unique=True)
    body = db.Column(db.String, unique=True)  # test icin unique false
    count = db.Column(db.Integer, unique=False)
    related = db.Column(db.String(64), unique=False)  # baska bir tabloya relation ver
    difficulty = db.Column(db.String(64), unique=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, title=None, body=None, count=None, related=None, difficulty=None):
        self.title = title
        self.body = body
        self.count = count
        self.related = related
        self.difficulty = difficulty
        self.slug = slugify(title)

    def __repr__(self):
        return '<Problems %r>' % (self.title)


roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    description = db.Column(db.String)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    username = db.Column(db.String(60), unique=True)
    time_registered = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    bio = db.Column(db.Text)
    avatar = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    roles = db.relationship(
        'Role', secondary=roles_users,
        backref=db.backref('users', lazy='dynamic'))

