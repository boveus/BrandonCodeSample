import os

from flask import Flask, flash, render_template, request, session
from sqlalchemy.orm import sessionmaker

from maketables import *

engine = create_engine('sqlite:///user.db', echo=True)

app = Flask(__name__)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello <a href='/logout'>Logout</a>"


@app.route('/login', methods=['POST'])
def do_admin_login():
    username = str(request.form['username'])
    password = str(request.form['password'])

    sql = ("SELECT password FROM USER \
       WHERE USERNAME = '%s'" % (username))

    this_session = sessionmaker(bind=engine)
    s = this_session()

    result = s.query(User).filter_by(username=username, password=password)

    if result.first:
        session['logged_in'] = True
    else:
        flash('incorrect login!')
    return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)