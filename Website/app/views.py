#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from app import app, db
from flask import request, g, render_template
import models, forms


@app.before_request
def before_request():
    g.request_start_time = time.time()
    g.request_time = lambda: "%.5fs" % (time.time() - g.request_start_time)


@app.route('/')
@app.route('/index')
def index():
    news = models.News.query.all()
    return render_template('index.html', title='Anasayfa', news=news)


@app.route('/news/<slug>')
def news(slug):
    post = models.News.query.filter_by(slug=slug).first()
    return render_template('news.html', title=post.title, post=post)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        form = forms.SignupForm(request.form)
        if form.validate():
            user = models.Users()
            form.populate_obj(user)
            user_exist = models.Users.query.filter_by(username=form.username.data).first()
            email_exist = models.Users.query.filter_by(email=form.email.data).first()
            if user_exist:
                form.username.errors.append('Username already taken')
            if email_exist:
                form.email.errors.append('Email already use')
            if user_exist or email_exist:
                return render_template('signup.html', form=form, title=u'Kayıt')
            else:
                db.session.add(user)
                db.session.commit()
                return render_template('signup-success.html', user=user, title=u'Kayıt Başarılı')
        else:
            return render_template('signup.html', form=form, title=u'Kayıt')
    return render_template('signup.html', form=forms.SignupForm(), title=u'Kayıt')


@app.route('/problems')
def problem_list():
    problems = models.Problems.query.all()
    return render_template('problem_list.html', title='Problem Listesi', problems=problems)


@app.route('/problem/<slug>')
def problem(slug):
    problem = models.Problems.query.filter_by(slug=slug).first()
    return render_template('problem.html', title=problem.title, problem=problem)



