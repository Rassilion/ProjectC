# -*- coding: utf-8 -*-
from app import db

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64),  unique=True)
    body = db.Column(db.String,  unique=True)
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return '<News %r>' % (self.title)

class Problems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64),  unique=True)
    slug = db.Column(db.String(64),  unique=True)
    body = db.Column(db.String,  unique=True)#test icin unique false
    count = db.Column(db.Integer,  unique=False)
    related=db.Column(db.String(64),  unique=False) #baska bir tabloya relation ver
    difficulty=db.Column(db.String(64),  unique=False)
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return '<Problems %r>' % (self.title)