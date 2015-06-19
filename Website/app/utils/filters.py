# -*- coding: utf-8 -*-
import datetime
from math import ceil
# Custom Template Filters
def datetimeformat(value):
    delta = datetime.datetime.now() - value
    if delta.days == 0:
        formatting = u'Bugün'
    elif delta.days < 10:
        formatting = u'{0} gün önce'.format(delta.days)
    elif delta.days < 28:
        formatting = u'{0} hafta önce'.format(int(ceil(delta.days/7.0)))
    else:
        formatting = u'%d.%m.%Y'
    return value.strftime(formatting.encode('utf-8')).decode('utf-8')