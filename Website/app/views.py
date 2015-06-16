#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from forms import *
from flask.ext.login import login_required
from flask.ext.security import Security, utils
from app import app,db
from flask import request, g, render_template, redirect, url_for, session
from models import User, Role, News, Problems,user_datastore
from admin import init_admin

#initilize flask-security
security = Security(app, user_datastore, register_form=ExtendedRegisterForm)

#page render time
@app.before_request
def before_request():
    # Create the Roles "admin" and "end-user" -- unless they already exist
    user_datastore.find_or_create_role(name='admin', description='Administrator')
    user_datastore.find_or_create_role(name='end-user', description='End user')

    # Create two Users for testing purposes -- unless they already exists.
    # In each case, use Flask-Security utility function to encrypt the password.
    encrypted_password = utils.encrypt_password('123456')
    if not user_datastore.get_user('user@user.com'):
        user_datastore.create_user(email='user@user.com',username='user', password=encrypted_password)
    if not user_datastore.get_user('admin@admin.com'):
        user_datastore.create_user(email='admin@admin.com',username='admin', password=encrypted_password)

    # Commit any database changes; the User and Roles must exist before we can add a Role to the User
    db.session.commit()

    # Give one User has the "end-user" role, while the other has the "admin" role. (This will have no effect if the
    # Users already have these Roles.) Again, commit any database changes.
    user_datastore.add_role_to_user('user@user.com', 'end-user')
    user_datastore.add_role_to_user('admin@admin.com', 'admin')
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
def problem(slug):
    problem = Problems.query.filter_by(slug=slug).first()
    return render_template('problem.html', title=problem.title, problem=problem)

@app.route('/problem/<slug>/solution')
@login_required
def problem_solution(slug):
    problem = Problems.query.filter_by(slug=slug).first()
    return render_template('problem_solution.html', title=problem.title, problem=problem)

@app.route('/problem/<slug>/suggestion')
@login_required
def problem_suggestion(slug):
    problem = Problems.query.filter_by(slug=slug).first()
    return render_template('problem.html', title=problem.title, problem=problem)

init_admin()