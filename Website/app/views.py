#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from flask.ext.login import login_required
from flask.ext.security import SQLAlchemyUserDatastore, Security
from flask.ext.security.utils import encrypt_password
from app import app, db
from flask import request, g, render_template, redirect, url_for, session
from forms import *
from models import User, Role, News, Problems

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


@app.before_request
def before_request():
    if not User.query.first():
        user_datastore.create_user(username='admin', password=encrypt_password('admin'), email='admin@gmail.com',
                                   bio='kral admin', avatar=None)
        db.session.commit()
    g.request_start_time = time.time()
    g.request_time = lambda: "%.5fs" % (time.time() - g.request_start_time)


@app.route('/')
@app.route('/index')
def index():
    news = News.query.all()
    return render_template('index.html', title='Anasayfa', news=news)


@app.route('/news/<slug>')
def news(slug):
    post = News.query.filter_by(slug=slug).first()
    return render_template('news.html', title=post.title, post=post)


@app.route('/problems')
def problem_list():
    problems = Problems.query.all()
    return render_template('problem_list.html', title='Problem Listesi', problems=problems)


@app.route('/problem/<slug>')
@login_required
def problem(slug):
    problem = Problems.query.filter_by(slug=slug).first()
    return render_template('problem.html', title=problem.title, problem=problem)



