# -*- coding: utf-8 -*-
from app import db

import datetime
from slugify import slugify



class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    slug = db.Column(db.String(64), unique=True)
    body = db.Column(db.String, unique=True)
    timestamp = db.Column(db.DateTime, default = datetime.datetime.utcnow)

    def __init__(self, title=None, body=None):
        self.title = title
        self.body = body
        self.slug = slugify(title)


    def __repr__(self):
        return '<News %r>' % (self.title)


class Problems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    slug = db.Column(db.String(64), unique=True)
    body = db.Column(db.String, unique=True)  # test icin unique false
    count = db.Column(db.Integer, unique=False)
    related = db.Column(db.String(64), unique=False)  # baska bir tabloya relation ver
    difficulty = db.Column(db.String(64), unique=False)
    timestamp = db.Column(db.DateTime,default = datetime.datetime.utcnow)

    def __init__(self, title=None, body=None, count=None, related=None, difficulty=None):
        self.title = title
        self.body = body
        self.count = count
        self.related = related
        self.difficulty = difficulty
        self.slug = slugify(title)

    def __repr__(self):
        return '<Problems %r>' % (self.title)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True)
    firstname = db.Column(db.String(20))
    lastname = db.Column(db.String(20))
    password = db.Column(db.String)
    email = db.Column(db.String(100), unique=True)
    time_registered = db.Column(db.DateTime,default = datetime.datetime.utcnow)
    bio = db.Column(db.Text)
    avatar = db.Column(db.String(255))

    def __init__(self, username=None, password=None,
                 email=None, firstname=None, lastname=None, bio=None, avatar=None):
        self.username = username
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.bio = bio
        self.avatar = avatar


    def __repr__(self):
        return '<User %r>' % (self.username)