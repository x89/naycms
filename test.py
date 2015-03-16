# Just toying around from the quickstart.
# http://flask.pocoo.org/docs/0.10/quickstart/#quickstart

from flask import (Flask, url_for, render_template, g, request, make_response,
session, redirect, flash)
app = Flask(__name__)

app.secret_key = 'pawkette'

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        session['user'] = request.form['username']
        flash('Hi %s!' % session['user'])
        return redirect(url_for('index'))
    else:
        if session.get('user'):
            flash("You've already logged in as %s" % session['user'])
            return redirect(url_for('index'))
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have logged out')
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.debug = True
    app.run()
