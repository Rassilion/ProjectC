#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from forms import *
from flask.ext.login import login_required
from flask.ext.security import Security, utils
from app import app, db
from flask import request, g, render_template, redirect, url_for, session, send_from_directory
from models import User, Role, News, Problem, user_datastore
from admin import init_admin

# initilize flask-security
security = Security(app, user_datastore, register_form=ExtendedRegisterForm)

# page render time
@app.before_request
def before_request():
    g.request_start_time = time.time()
    g.request_time = lambda: "%.5fs" % (time.time() - g.request_start_time)


# search engine things
@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route('/')
@app.route('/index')
def index():
    news = News.query.all()
    return render_template('index.html', title='Anasayfa', news=news)


@app.route('/about')
def about():
    return render_template('about.html', title=u'Hakkında')


@app.route('/news/<slug>')
def news(slug):
    post = News.query.filter_by(slug=slug).first_or_404()
    return render_template('news.html', title=post.title, post=post)


@app.route('/problems')
def problem_list():
    problems = Problem.query.all()
    return render_template('problem_list.html', title='Problem Listesi', problems=problems)


@app.route('/problem/<slug>')
def problem(slug):
    problem = Problem.query.filter_by(slug=slug).first_or_404()
    return render_template('problem.html', title=problem.title, problem=problem)


@app.route('/problem/<slug>/solution')
@login_required
def problem_solution(slug):
    problem = Problem.query.filter_by(slug=slug).first_or_404()
    return render_template('problem_solution.html', title=problem.title, problem=problem)


@app.route('/problem/<slug>/suggestion')
@login_required
def problem_suggestion(slug):
    problem = Problem.query.filter_by(slug=slug).first_or_404()
    return render_template('problem.html', title=problem.title, problem=problem)


@app.route('/author/<username>')
def author_profile(username):
    author = User.query.filter_by(username=username).first_or_404()
    problems = author.problems
    return render_template('author_profile.html', title=author.username,author=author, problems=problems)


init_admin()
