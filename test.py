# Just toying around from the quickstart.
# http://flask.pocoo.org/docs/0.10/quickstart/#quickstart

from flask import (Flask, url_for, render_template, g, request, make_response,
session, redirect, flash)
app = Flask(__name__)

app.secret_key = 'pawkette'

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/foo/<int:foo>")
def bar(foo):
    if foo == 5:
        return url_for('static', filename="style.css")
    else:
        return str(foo * 2)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        session['user'] = request.form['username']
        return redirect(url_for('index'))
    else:
        if session.get('user'):
            return "Already logged in as %s." % session['user']
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have logged out.')
    return redirect(url_for('index'))

@app.route("/user/<username>")
def user(username):
    return render_template("user.html", user=username)

if __name__ == "__main__":
    app.debug = True
    app.run()
