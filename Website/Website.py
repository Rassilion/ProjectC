from flask import *

app = Flask(__name__)
app.config.from_pyfile('config.cfg', silent=True)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/problems')
def problems():
    return render_template('problem_list.html')


if __name__ == '__main__':
    app.run()
