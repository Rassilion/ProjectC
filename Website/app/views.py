#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from sqlalchemy import desc
from forms import *
from flask.ext.login import login_required
from flask.ext.security import Security, utils
from app import app, db
from app.utils.table import Table
from flask import request, g, render_template, redirect, url_for, session, send_from_directory
from models import *
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


@app.route('/problems/')
@app.route('/problems/<int:page>')
def problem_list(page=1):
    problems = sort(Problem, Problem.query, problem_sort_list).paginate(
        page=page, per_page=app.config["PRODUCTS_PER_PAGE"],
    )
    problems_table = Table(problem_sort_list, problem_column_list, problems)
    return render_template('problem_list.html', title='Problem Listesi', problems_table=problems_table)


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


@app.route('/author/<username>/')
@app.route('/author/<username>/<int:page>')
def author_profile(username, page=1):
    author = User.query.filter_by(username=username).first_or_404()
    problems = sort(Problem, author.problems, problem_sort_list).paginate(
        page=page, per_page=app.config["PRODUCTS_PER_PAGE"],
    )
    problems_table = Table(problem_sort_list, problem_column_list, problems)
    return render_template('author_profile.html', title=author.username, author=author, problems_table=problems_table)


@app.route('/tag/<name>/')
@app.route('/tag/<name>/<int:page>')
def tag(name, page=1):
    tag = Tag.query.filter_by(name=name).first_or_404()
    problems = sort(Problem, tag.problems, problem_sort_list).paginate(
        page=page, per_page=app.config["PRODUCTS_PER_PAGE"],
    )
    problems_table = Table(problem_sort_list, problem_column_list, problems)
    return render_template('tag.html', title=tag.name, tag=tag, problems_table=problems_table)


@app.route('/user/<username>')
def user_profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    # order submissions by timestamp
    submissions = user.submissions.order_by(Submission.timestamp.desc())
    return render_template('user_profile.html', title=user.username, user=user, submissions=submissions)


problem_sort_list = {'id', 'title', 'count', 'difficulty'}
problem_column_list = [('id', u'id'), ('title', u'başlık'), ('tags', u'İlgili konular'), ('count', u'Çözüm sayısı'), (
    'difficulty', u'Zorluk')]


def sort(model, query, sort_list):
    """
    sort query with url args

    :param model:
    db model name
    :param query:
    sql alchemy query
    :param sort_list:
    allowed sort url args
    :return:
    sorted query if fails return query
    """
    sort = request.args.get('sort', 'id')
    sort_desc = request.args.get('desc', 0, type=int)
    if sort not in sort_list:
        return query
    if sort_desc == 1:
        return query.order_by(desc(getattr(model, sort)))
    else:
        return query.order_by(getattr(model, sort))



init_admin()
