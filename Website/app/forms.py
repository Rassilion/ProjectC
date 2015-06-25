# !/usr/bin/python
# -*- coding: utf-8 -*-
from flask_security.forms import RegisterForm, Required
from flask_wtf import Form
from wtforms import TextField
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField
from models import Tag, Problem
from wtforms_alchemy import ModelForm


class ExtendedRegisterForm(RegisterForm):
    username = TextField('Username', [Required()])


def tags():
    return Tag.query.order_by(Tag.name).all()


class ProblemForm(ModelForm, Form):
    class Meta:
        model = Problem
        only = ['title', 'body', 'solution', 'difficulty']

    tags = QuerySelectMultipleField(u'İlgili konular', query_factory=tags)
