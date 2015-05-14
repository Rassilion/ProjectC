# !/usr/bin/python
# -*- coding: utf-8 -*-from flask.ext.wtf import Form
from flask_security.forms import RegisterForm, Required, TextField


class ExtendedRegisterForm(RegisterForm):
    username = TextField('Username', [Required()])