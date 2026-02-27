from flask import Flask

from flask import render_template
app = Flask(__name__, static_url_path="/static")


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)

@app.route("/")
def hello_world(name=None):
    return render_template('hey.html', person=name)
