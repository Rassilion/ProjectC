#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time
from app import app
from flask import request, g, render_template
import models


@app.before_request
def before_request():
    g.request_start_time = time.time()
    g.request_time = lambda: "%.5fs" % (time.time() - g.request_start_time)


@app.route('/')
@app.route('/index')
def index():
    news = models.News.query.all()
    return render_template('index.html',title='Anasayfa', news=news)

@app.route('/news/<slug>')
def news(slug):
    post = models.News.query.filter_by(slug=slug).first()
    return render_template('news.html',title=post.title, post=post)

@app.route('/problems')
def problem_list():
    problems = models.Problems.query.all()
    return render_template('problem_list.html',title='Problem Listesi', problems=problems)


@app.route('/problem/<slug>')
def problem(slug):
    problem = models.Problems.query.filter_by(slug=slug).first()
    return render_template('problem.html',title=problem.title, problem=problem)



