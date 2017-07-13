#!/usr/bin/python
# -*- coding: utf-8 -*-
from sqlalchemy_wrapper import SQLAlchemy
from config import *
from redis import StrictRedis

r = StrictRedis(host=REDIS_SERVICE, port=6379, db=0)
p = r.pubsub(ignore_subscribe_messages=True)
p.psubscribe('submissions')
db = SQLAlchemy(SQLALCHEMY_DATABASE_URI)
