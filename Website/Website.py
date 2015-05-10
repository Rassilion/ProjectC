#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time
from flask import Flask, request, g, render_template


app = Flask(__name__)
app.config.from_pyfile('config.cfg', silent=True)


@app.before_request
def before_request():
    g.request_start_time = time.time()
    g.request_time = lambda: "%.5fs" % (time.time() - g.request_start_time)


@app.route('/')
@app.route('/index')
def index():
    news = [{'title': 'Duyuru 1',
             'body': '<p>One must discover the sun in order to shape the doer of honorable mineral. Trust happens when you trap music so substantially that whatsoever you are easing is your pain. One must gain the lama in order to facilitate the cow of secret heaven. One must hurt the explosion of the anger in order to love the spirit of unconditional career. When the follower of resurrection knows the tantras of the lama, the politics will know power.<//p>'},
            {'title': 'Duyuru 2',
             'body': '<p>Nunquam carpseris lapsus. Magnum, altus lunas vix acquirere de alter, mirabilis lapsus. Bassus, azureus vortexs aegre experientia de grandis, velox canis. Amicitia de camerarius assimilatio, experientia armarium! Ubi est lotus sensorem? Cum danista cadunt, omnes fortises demitto salvus, pius cannabises. Elevatus, medicina, et mensa. Cum sectam mori, omnes tuses captis fidelis, bi-color cobaltumes. Assimilant recte ducunt ad regius fraticinida. Audax, festus habitios nunquam locus de castus, altus clabulare.<//p>'}]
    return render_template('index.html', news=news)


@app.route('/problems')
def problem_list():
    problems = [
        {'id': '1', 'title': 'Mükemmel sayı', 'slug': 'mukemmel_sayi', 'releted': 'Basic Operations', 'count': '209',
         'dificulty': '1'},
        {'id': '2', 'title': 'İlginç döngüler', 'slug': 'ılgınc_dongu', 'releted': 'Basic Operations', 'count': '280',
         'dificulty': '3'},
        {'id': '3', 'title': 'Bozuk sayı', 'slug': 'bozuk_sayi', 'releted': 'Basic Operations', 'count': '250',
         'dificulty': '4'},
        {'id': '4', 'title': 'Güzel sayı', 'slug': 'guzel_sayi', 'releted': 'Basic Operations', 'count': '202',
         'dificulty': '5'},
        {'id': '5', 'title': 'Mükemmel sayı', 'slug': 'mukemmel_sayi', 'releted': 'Basic Operations', 'count': '20',
         'dificulty': '1'}
        , {'id': '6', 'title': 'Mükemmel sayı', 'slug': 'mukemmel_sayi', 'releted': 'Basic Operations', 'count': '20',
           'dificulty': '1'}]
    return render_template('problem_list.html', problems=problems)


@app.route('/problem/<slug>')
def problem(slug):
    problems = [
        {'id': '1', 'title': 'Mükemmel sayı', 'slug': 'mukemmel_sayi', 'releted': 'Basic Operations', 'count': '209',
         'dificulty': '1',
         'body': '<p>Kendi hariç bütün sayıları....</p><p>Girdi: asdsadsad</p><p>Çıktı: asdsadsa</p><div class="panel panel-default"><div class="panel-heading"><h3 class="panel-title">Örnek Girdi</h3></div><div class="panel-body">28</div></div><div class="panel panel-default"><div class="panel-heading"><h3 class="panel-title">Örnek Çıktı</h3></div><div class="panel-body">EVET</div></div>'}]
    return render_template('problem.html', problem=problems[0])


if __name__ == '__main__':
    app.debug = True
    app.run()
